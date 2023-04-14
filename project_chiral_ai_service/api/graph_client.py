from project_chiral_ai_service.api.graph_api.api.default_api import DefaultApi
from project_chiral_ai_service.api.graph_api.api_client import ApiClient
from project_chiral_ai_service.api.graph_api.configuration import Configuration


class GraphClient(DefaultApi):
    def __init__(self):
        super().__init__(api_client=ApiClient(
            configuration=Configuration(
                host="http://localhost:4001"
            )
        ))

    def close(self):
        self.api_client.close()