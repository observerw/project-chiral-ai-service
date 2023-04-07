from haystack.document_stores.faiss import FAISSDocumentStore

from project_chiral_ai_service.constant import *


class DocumentStore(FAISSDocumentStore):
    def __init__(self):
        super().__init__(
            similarity="dot_product",
            embedding_dim=768,
            sql_url=FAISS_URL,
            faiss_index_factory_str="Flat",
            return_embedding=True,
        )
