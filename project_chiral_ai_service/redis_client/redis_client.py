from typing import List

import redis

from project_chiral_ai_service.constant import *
from project_chiral_ai_service.redis_client.constant import CharaTable


class RedisClient:
    def __init__(self) -> None:
        self.conn = None

    def connect(self):
        self.conn = redis.StrictRedis(
            host=REDIS_HOST,
            port=REDIS_PORT,
            password=REDIS_PASSWORD,
        )

    def close(self):
        self.conn.close()

    def get_all_characters(self, project_id: int) -> List[str]:
        return self.conn.hkeys(CharaTable(project_id))

    def get_character_id(self, project_id: int, chara_name: str):
        id = self.conn.hget(CharaTable(project_id), chara_name)
        if id is None:
            return -1
        return int(id)
