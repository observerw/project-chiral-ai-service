import spacy


class EntityRecognizer:
    def __init__(self) -> None:
        self.model = spacy.load("zh_core_web_trf")

    def process(self, text: str):
        doc = self.model(text)

        return [ent for ent in doc.ents if ent.label_ == "PERSON"]


if __name__ == "__main__":
    recognizer = EntityRecognizer()

    result = recognizer.process(
        "战争中丘吉尔首相与苏联领导人斯大林的关系十分特殊，因为首相素来持有鲜明的反共立场，但是在二战中受形势所迫，只能与斯大林合作才能对抗迅速膨胀的纳粹德国。1941年6月22日，德国向苏联宣战的当晚，丘吉尔就向全国民众发表演说称：“在过去的25年中，没有一个人像我那样始终一贯地反对共产主义。我并不想收回我说过的话，但是这一切在正在我们眼前展现的情景对照之下，都已黯然失色了……任何对第三帝国作战的个人或国家，都将得到我们的援助。任何跟着希特勒走的个人或国家，都是我们的敌人。”")

    print(result)
