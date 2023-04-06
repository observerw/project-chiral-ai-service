from project_chiral_ai_service.summarize.template import TitlePromptParams


def test_basic():
    a = TitlePromptParams(**{
        'doc': '测试'
    })

    print(a.dict())

    assert a is not None
