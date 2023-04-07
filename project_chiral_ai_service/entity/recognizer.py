import json

from haystack.nodes import PromptNode

from project_chiral_ai_service.constant import *
from project_chiral_ai_service.entity.template import entity_template, EntityPromptParams
from project_chiral_ai_service.rmq_client.response import RmqResponse


class EntityRecognizer:
    def __init__(self) -> None:
        self.node = PromptNode(
            model_name_or_path=ENTITY_MODEL,
            api_key=OPENAI_API_KEY,
            max_length=512,
            default_prompt_template=entity_template,
        )

    def process(self, params):
        params = EntityPromptParams(**params)
        result = self.node.prompt(**params.dict())[0]
        result = json.loads(result)

        return RmqResponse(data=result)
