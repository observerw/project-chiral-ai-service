from haystack.nodes import EmbeddingRetriever

from project_chiral_ai_service.constant import *
from project_chiral_ai_service.retriever.document_store import DocumentStore


class Retriever(EmbeddingRetriever):
    def __init__(self):
        document_store = DocumentStore()
        super().__init__(
            document_store=document_store,
            embedding_model=RETRIEVE_MODEL,
            batch_size=16,
            api_key=OPENAI_API_KEY,
            max_seq_len=1024
        )
