import os

from dotenv import load_dotenv

load_dotenv()

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

POSTGRES_USERNAME = os.environ["POSTGRES_USERNAME"]
POSTGRES_PASSWORD = os.environ["POSTGRES_PASSWORD"]
POSTGRES_HOST = os.environ["POSTGRES_HOST"]
POSTGRES_PORT = os.environ["POSTGRES_PORT"]
POSTGRES_DB = os.environ["POSTGRES_DB"]
POSTGRES_SCHEMA = os.environ["POSTGRES_SCHEMA"]
DATABASE_URL = os.environ["DATABASE_URL"]
NEO_URL = os.environ["NEO_URL"]
NEO_USERNAME = os.environ["NEO_USERNAME"]
NEO_PASSWORD = os.environ["NEO_PASSWORD"]
RMQ_HOST = os.environ["RMQ_HOST"]
RMQ_PORT = os.environ["RMQ_PORT"]
RMQ_USERNAME = os.environ["RMQ_USERNAME"]
RMQ_PASSWORD = os.environ["RMQ_PASSWORD"]
RMQ_URI = os.environ["RMQ_URI"]
RMQ_QUEUE = os.environ["RMQ_QUEUE"]
OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
REDIS_HOST = os.environ["REDIS_HOST"]
REDIS_PORT = os.environ["REDIS_PORT"]
REDIS_PASSWORD = os.environ["REDIS_PASSWORD"]
REDIS_URL = os.environ["REDIS_URL"]

FAISS_URL = f"postgresql://{POSTGRES_USERNAME}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/faiss"
FAISS_INDEX_PATH = os.path.join(ROOT_PATH, "faiss_index.faiss")
FAISS_CONFIG_PATH = os.path.join(ROOT_PATH, "faiss_config.json")

SUMMARIZE_MODEL = "gpt-3.5-turbo"
EMBEDDING_MODEL = "ada"
ENTITY_MODEL = "gpt-3.5-turbo"

LANG_MAP = {
    'cn': 'Chinese Simplified',
    'en': 'English',
}
