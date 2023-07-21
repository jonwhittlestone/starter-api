import pytest

from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine
from sqlmodel.pool import StaticPool


@pytest.fixture(name="session")
def session_fixture():
    # in memory db
    engine = create_engine(
        "sqlite://",  #
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,  #
    )
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session


@pytest.fixture(name="client")  #
def client_fixture(session: Session):  #
    def get_session_override():  #
        return session
