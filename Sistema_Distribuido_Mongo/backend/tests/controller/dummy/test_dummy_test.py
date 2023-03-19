from typing import Final

import pytest
from fastapi import status
from fastapi.testclient import TestClient
from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.database.models import DummyTestDB
from backend.tests.factories import DummyTestFactory

URL: Final[str] = "/api/dummy_test/"


def test_should_return_ok(
    client: TestClient, db_session: Session, monkeypatch: pytest.MonkeyPatch
) -> None:
    # Arrange
    dummy = DummyTestFactory()

    # Act
    response = client.post(URL, json=dummy.dict())

    # Assert
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == dummy

    dummies_db = db_session.execute(select(DummyTestDB)).unique().scalars().all()
    assert len(dummies_db) == 1
