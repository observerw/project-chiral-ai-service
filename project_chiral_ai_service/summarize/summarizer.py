from haystack.nodes import PromptNode

from project_chiral_ai_service.constant import *
from project_chiral_ai_service.rmq_client.response import RmqResponse
from project_chiral_ai_service.summarize.template import title_template, desc_template, TitlePromptParams, \
    DescPromptParams
from project_chiral_ai_service.summarize.utils import summarize_length


class Summarizer:
    def __init__(self) -> None:
        self.node = PromptNode(
            model_name_or_path=SUMMARIZE_MODEL,
            api_key=OPENAI_API_KEY,
            max_length=512,
        )
        print('summarizer ready')

    def summarize_title(self, params):
        params = TitlePromptParams(**params)
        return RmqResponse(
            data=self.node.prompt(prompt_template=title_template, **params.dict())[0]
        )

    def summarize_desc(self, params):
        params = DescPromptParams(**params)
        params.keyword = ''.join(params.keyword)

        if params.length is None:
            params.length = summarize_length(params.doc)

        if params.length == len(params.doc):
            return RmqResponse(data=params.doc)
        else:
            return RmqResponse(data=self.node.prompt(
                prompt_template=desc_template,
                **params.dict()
            )[0])
