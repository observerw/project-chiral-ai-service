from typing import List

from pydantic import BaseModel

from project_chiral_ai_service.entity.linker import EntityLinker, CharaItem
from project_chiral_ai_service.entity.recognizer import EntityRecognizer
from project_chiral_ai_service.entity.template import EntityPromptParams


class EntityResolveReq(BaseModel):
    table: List[CharaItem]
    doc: str
    lang: str


class EntityResolver:
    def __init__(self):
        self.recognizer = EntityRecognizer()
        self.linker = EntityLinker()

    def process(self, params: EntityResolveReq):
        names = self.recognizer.process(EntityPromptParams(doc=params.doc))
        options = [
            {name: self.linker.process(table=params.table, name=name, lang=params.lang)}
            for name in names
        ]

        return options


if __name__ == "__main__":
    recognizer = EntityRecognizer()
    linker = EntityLinker()
    resolver = EntityResolver()

    result = resolver.process(EntityResolveReq(
        table=[
            CharaItem(id=1, name='木之本樱', alias=['小樱', '魔卡少女']),
            CharaItem(id=2, name='大道寺知世', alias=[]),
            CharaItem(id=3, name='可鲁贝洛斯', alias=['小可']),
        ],
        lang='cn',
        doc="""小樱做了不可思议的预知梦。在梦中，小樱面对的是谁……等待凭借预知梦走向东京铁塔的小樱等人的是……友枝町突然被黑暗笼罩，街上的人们都睡了过去。清晨之前若不能打破魔法，人们就会如此沉睡不醒。小樱和可鲁贝洛斯决定前往友枝町，但是在路上遇到了知世。知世说他也是为了打破魔法而来，但是他的目的是为了拯救自己的妹妹。小樱和可鲁贝洛斯决定与知世一起前往友枝町。"""
    ))

    print(result)
