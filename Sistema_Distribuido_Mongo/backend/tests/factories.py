from factory import Factory, fuzzy

from backend.schemas.musica_schema import MusicaTest

class MusicaFactory(Factory):  # type: ignore[misc]
    class Meta:
        model = MusicaTest

    title = fuzzy.FuzzyText(length=20)
    director = fuzzy.FuzzyText(length=20)
