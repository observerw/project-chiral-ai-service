from prisma import Prisma
from pydantic import BaseModel

from project_chiral_ai_service.retriever import Retriever


class EventDoneReq(BaseModel):
    id: int
    done: bool


def event_done_process(prisma: Prisma, retriever: Retriever):
    def inner(body):
        return None

    return inner
