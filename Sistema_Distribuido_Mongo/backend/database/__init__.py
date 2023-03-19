from typing import cast

from fastapi import Request
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

from sqlalchemy.orm import sessionmaker, Session

from backend.settings import Environment

MAIN_ENGINE: Engine
SESSION_MAKER: Session


def init_database(env: Environment) -> None:
    global MAIN_ENGINE, SESSION_MAKER
    MAIN_ENGINE = create_engine(env.db_main_uri, echo=False, future=True)
    SESSION_MAKER = sessionmaker(MAIN_ENGINE, future=True)


def get_sessions(request: Request) -> Session:
    return cast(Session, request.state.db_session)
