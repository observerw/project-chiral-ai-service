from prisma import Prisma

from project_chiral_ai_service.rmq_client import RmqClient
from project_chiral_ai_service.summarize import Summarizer

prisma = Prisma()

summarizer = Summarizer(prisma=prisma)

rmq_client = RmqClient(
    handlers={
        'summarize_title': summarizer.summarize_title,
        'summarize_desc': summarizer.summarize_desc,
    }
)


def main():
    rmq_client.connect()


def close():
    rmq_client.close()
    print('shutdown')


if __name__ == "__main__":
    try:
        main()
    finally:
        close()
