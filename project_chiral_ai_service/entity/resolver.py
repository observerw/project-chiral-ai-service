import math
from typing import List

from pydantic import BaseModel

from project_chiral_ai_service.entity.linker import EntityLinker, CharaItem, LinkOption
from project_chiral_ai_service.entity.recognizer import EntityRecognizer
from project_chiral_ai_service.entity.template import EntityPromptParams
from project_chiral_ai_service.schema import LangType, LANG_MAP


class EntityResolveReq(BaseModel):
    table: List[CharaItem]
    doc: str
    lang: LangType


class Resolved(BaseModel):
    id: int


class Unresolved(BaseModel):
    name: str
    options: List[LinkOption]


class EntityResolveResp(BaseModel):
    resolved: List[Resolved] = []
    unresolved: List[Unresolved] = []


class EntityResolver:
    def __init__(self):
        self.recognizer = EntityRecognizer()
        self.linker = EntityLinker()

    def process(self, params: EntityResolveReq):
        names = self.recognizer.process(EntityPromptParams(doc=params.doc))
        result = EntityResolveResp()

        for name in names:
            options = self.linker.process(table=params.table, name=name, lang=params.lang)

            # 分数为1，完全匹配
            if any([math.fabs(option.score - 1) < 1e-6 for option in options]):
                result.resolved.append(Resolved(
                    id=options[0].id
                ))
            else:
                result.unresolved.append(Unresolved(
                    name=name,
                    options=options
                ))

        # 去重
        result.resolved = list({item.id: item for item in result.resolved}.values())

        return result


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
        lang=LANG_MAP['cn'],
        doc="""小樱做了不可思议的预知梦。在梦中，小樱面对的是谁……等待凭借预知梦走向东京铁塔的小樱和小可等人的是……友枝町突然被黑暗笼罩，街上的人们都睡了过去。清晨之前若不能打破魔法，人们就会如此沉睡不醒。小樱和可鲁贝洛斯决定前往友枝町，但是在路上遇到了知世。知世说他也是为了打破魔法而来，但是他的目的是为了拯救自己的妹妹。小樱和可鲁贝洛斯决定与知世一起前往友枝町。"""
    ))

    print(result)
