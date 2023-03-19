from typing import Iterator

from pytest import fixture
from sqlalchemy.orm import close_all_sessions

from audited_db.session import DatabaseSessions, SessionMaker
from audited_db.util import truncate
from backend import database
from backend.database.models import Base as BaseMain
from backend.settings import Environment


@fixture(name="env", scope="session")
def _env() -> Environment:
    return Environment(_env_file="tests.env")


@fixture(name="init_db", scope="session")
def _init_db(env: Environment) -> None:
    database.init_database(env)
    BaseMain.metadata.create_all(database.MAIN_ENGINE)
    database.SESSION_MAKER.configure(expire_on_commit=False)


@fixture(name="session_maker", scope="function")
def _session_maker(init_db: None) -> Iterator[SessionMaker]:  # pylint: disable=unused-argument
    """
    This fixture provides a `SessionMaker`, allowing for the control of transactions, with auto-truncate on teardown.
    Use the `db_sessions` fixture for tests that don't span across transactions.
    """
    yield database.SESSION_MAKER
    close_all_sessions()
    truncate(database.MAIN_ENGINE)


@fixture(name="db_session", scope="function")
def _db_session(init_db: None) -> Iterator[DatabaseSessions]:  # pylint: disable=unused-argument
    """
    This fixture provides a SQLAlchemy `Session`, which is effectively a database transaction,
    with auto-rollback on teardown.
    Hence, it will generally be used in tests that don't span across transactions.
    Use the `session_maker` fixture for tests that need control over the transactions.
    """
    with database.SESSION_MAKER.begin() as session:
        # dbfactories.configure_session(session.main)
        yield session
        session.rollback()
