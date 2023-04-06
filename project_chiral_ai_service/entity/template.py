from haystack.nodes import PromptTemplate
from pydantic import BaseModel

entity_template = PromptTemplate(
    name="entity",
    prompt_text="You are tasked with developing a named entity recognizer that can extract the names of historical figures from user-provided historical texts. The texts are similar to history textbooks and may include specific details such as characters, time, and events, as well as subjective text and literary descriptions. Your need to accurately identify and extract the names of important people mentioned in the texts, regardless of their cultural background or time period. The program should prioritize accurately identifying recognizable names, even if some difficult-to-recognize names may be left unrecognized. The final product should output a JSON array containing each identified historical figure's name, with duplicate elements removed. Results should be in {lang}.",
)


class EntityPromptParams(BaseModel):
    lang: str
