from pydantic import BaseModel

LANG_MAP = {
    'en': 'English',
    'cn': 'Chinese Simplified',
}


class LangType(str):

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(enum=LANG_MAP.keys())

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        return LANG_MAP.get(v, v)


class Test(BaseModel):
    lang: LangType


if __name__ == "__main__":
    t = Test(lang='cn')
    print(t.lang)
