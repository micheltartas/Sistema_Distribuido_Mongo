from fastapi.testclient import TestClient
from pytest import fixture

from audited_db.session import SessionMaker
from backend.main import app
from backend.settings import Environment, get_environment


@fixture(name="client", scope="function")
def _client(
    env: Environment,
) -> TestClient:
    app.dependency_overrides[get_environment] = lambda: env
    return TestClient(app, raise_server_exceptions=False)


@fixture(name="session_maker", scope="function", autouse=True)
def _session_maker(session_maker: SessionMaker) -> SessionMaker:
    """
    Just overrides the "global" session_maker fixture so that controller tests
    automatically use them, guaranteeing that the database is truncated.
    """
    return session_maker
