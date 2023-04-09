from typing import Optional, List

from haystack.nodes import PromptTemplate
from pydantic import BaseModel

from project_chiral_ai_service.constant import *

title_template = PromptTemplate(
    name="summarize_title",
    prompt_text=
    """Provide a short, descriptive title for the given piece of document. The title needs to be in the same language as the original text.
    [document]
    {doc}
                
    [title]""",
)


class TitlePromptParams(BaseModel):
    doc: str


desc_template = PromptTemplate(
    name="summarize_desc",
    prompt_text=
    """[document]
    {doc}
    
    [instructions]
    Develop a text summarizer that can condense historical texts into informative, concise summaries. The summarizer should detect language of the input text and output summaries that are no longer than a specified length of {length}. The summarizer should strive to accurately capture specific details such as names, dates, and locations in the original text. The summary should be generated around a set of specified keywords: {keyword}, which represents a group of character names. The summarizer should maintain a professional tone and achieve a minimum level of abstraction, indicated by {abstraction}, by limiting the percentage of directly copied sentences from the original text. The input texts may include subjective or literary descriptions. The output format for the summaries should be a single paragraph. The summaries needs to be in {lang}.
    
    [output]"""
)


class DescPromptParams(BaseModel):
    doc: str
    lang: str = LANG_MAP['cn']
    length: Optional[int] = None
    abstraction: int = 70
    keyword: List[str] = []
