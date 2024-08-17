from database import dependencies, orm
from domain import request, response
from service import service
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

LOCALHOST_DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/cache_service"
engine = create_engine(LOCALHOST_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

orm.Base.metadata.create_all(bind=engine)


def test_add_payload_service():
    db_session = SessionLocal()

    request_obj = request.PayloadRequest(
        list_1=["first_string", "second_string", "third_string"],
        list_2=["fourth_string", "fifth_string"],
    )
    payload = service.add_payload(db_session, request_obj)

    assert payload["id"] is not None
    assert payload["value"] == service.transform_value(request_obj)

    db_session.close()
