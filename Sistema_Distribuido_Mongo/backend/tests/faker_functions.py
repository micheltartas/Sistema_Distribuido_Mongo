from typing import Any, cast

from faker import Faker

fake = Faker()


def fake_dict() -> dict[str, Any]:
    return cast(dict[str, Any], fake.pydict())
