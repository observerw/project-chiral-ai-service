from typing import List

import Levenshtein
from pydantic import BaseModel

from project_chiral_ai_service.schema import LANG_MAP


def LCS(a: str, b: str) -> int:
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_len = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                max_len = max(max_len, dp[i][j])
            else:
                dp[i][j] = 0
    return max_len


def calc_score(lang: str, name: str, exist_name: str) -> float:
    if lang == LANG_MAP['cn']:
        return LCS(name, exist_name) / max(len(name), len(exist_name))

    if lang == LANG_MAP['en']:
        return Levenshtein.ratio(name.lower(), exist_name.lower())


class CharaItem(BaseModel):
    id: int
    name: str
    alias: List[str] = []


class LinkOption(BaseModel):
    id: int
    name: str
    alias: str
    score: float


class EntityLinker:
    def __init__(self):
        pass

    @staticmethod
    def process(table: List[CharaItem], name: str, lang: str) -> List[LinkOption]:
        options = []

        for item in table:
            exists_names = [item.name] + item.alias

            # 取最高分数
            score = 0
            alias = None
            for exist_name in exists_names:
                cur_score = calc_score(lang, name, exist_name)
                if cur_score > score:
                    score = cur_score
                    alias = exist_name

            if score == 0:
                continue

            options.append(LinkOption(
                id=item.id,
                name=item.name,
                alias=alias,
                score=score
            ))

        options.sort(key=lambda x: x.score, reverse=True)
        return options


if __name__ == "__main__":
    linker = EntityLinker()

    result = linker.process(
        table=[
            CharaItem(id=1, name='木之本樱', alias=['小樱', '魔卡少女']),
            CharaItem(id=2, name='大道寺知世', alias=[]),
            CharaItem(id=3, name='可鲁贝洛斯', alias=['小可']),
        ],
        name='小可',
        lang=LANG_MAP['cn']
    )

    print(result)
