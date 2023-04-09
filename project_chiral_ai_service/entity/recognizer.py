import json

from haystack.nodes import PromptNode

from project_chiral_ai_service.constant import *
from project_chiral_ai_service.entity.template import entity_template, EntityPromptParams


class EntityRecognizer:
    def __init__(self) -> None:
        self.node = PromptNode(
            model_name_or_path=ENTITY_MODEL,
            api_key=OPENAI_API_KEY,
            max_length=512,
            default_prompt_template=entity_template,
        )

    def process(self, params: EntityPromptParams):
        result: str = self.node.prompt(**params.dict(), prompt_template=entity_template)[0]
        result = result.replace('\'', '\"')
        result = json.loads(result)

        return result
