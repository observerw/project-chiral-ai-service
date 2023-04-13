from prisma import Prisma
from pydantic import BaseModel

from project_chiral_ai_service.entity import EntityResolver, EntityResolveReq
from project_chiral_ai_service.retriever import Retriever
from project_chiral_ai_service.rmq_client import RmqClient, RpcHandler, SubscribeHandler
from project_chiral_ai_service.subscribe import event_done_process, EventDoneReq
from project_chiral_ai_service.summarize import Summarizer, SummarizeTitleReq, SummarizeDescReq

prisma = Prisma()

summarizer = Summarizer()
entity_resolver = EntityResolver()

retriever = Retriever()


def temp(body):
    print(body)


class TempReq(BaseModel):
    done: bool
    id: int


rmq_client = RmqClient(
    rpc_handlers={
        'summarize_title': RpcHandler(
            process=summarizer.summarize_title,
            request=SummarizeTitleReq,
        ),
        'summarize_desc': RpcHandler(
            process=summarizer.summarize_desc,
            request=SummarizeDescReq,
        ),
        'entity_resolve': RpcHandler(
            process=entity_resolver.process,
            request=EntityResolveReq,
        )
    },
    subscribe_handlers={
        'event-done': SubscribeHandler(
            process=event_done_process(prisma, retriever),
            request=EventDoneReq,
        )
    }
)


def main():
    prisma.connect()
    rmq_client.connect()


def close():
    prisma.disconnect()
    retriever.close()
    rmq_client.close()
    print('shutdown')


if __name__ == "__main__":
    try:
        main()
    finally:
        close()
