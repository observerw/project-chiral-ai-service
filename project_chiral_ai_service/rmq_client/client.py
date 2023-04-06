import json
import os
from typing import Dict, Callable

import pika


def _handle_request(fn: Callable):
    def inner(ch, method, props, body):
        print(f"receive request: {body.decode('utf-8')}")
        body = str(body.decode("utf-8"))
        body = json.loads(body)
        resp = fn(body)
        resp = resp.json()

        ch.basic_publish(
            exchange='',
            routing_key=props.reply_to,
            properties=pika.BasicProperties(
                correlation_id=props.correlation_id
            ),
            body=resp
        )
        ch.basic_ack(delivery_tag=method.delivery_tag)
        print(f"response with: {resp}")

    return inner


class RmqClient:
    def __init__(self, handlers: Dict[str, callable]) -> None:
        self.conn = None
        self.channel = None
        self.handlers = handlers

    def connect(self):
        credentials = pika.PlainCredentials(
            username=os.environ['RMQ_USERNAME'],
            password=os.environ['RMQ_PASSWORD'],
            erase_on_connect=True
        )
        self.conn = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=os.environ['RMQ_HOST'],
                port=int(os.environ['RMQ_PORT']),
                credentials=credentials
            )
        )
        self.channel = self.conn.channel()
        for queue in self.handlers.keys():
            self.channel.queue_declare(queue=queue)
            handler = _handle_request(self.handlers[queue])
            self.channel.basic_consume(
                queue=queue,
                on_message_callback=handler,
            )

        print('rmq_client connected')
        self.channel.start_consuming()

    def close(self):
        if self.channel is None or self.conn is None:
            return
        self.channel.close()
        self.conn.close()
