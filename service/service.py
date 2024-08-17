import redis
import os
import dotenv
import json

from sqlalchemy.orm import Session

from database import orm
from domain import request


dotenv.load_dotenv(verbose=True)

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis_cache"),
    port=int(os.getenv("REDIS_PORT", 6381)),
    db=0,
)


def add_payload(session: Session, request: request.PayloadRequest):
    payload = orm.PayloadData(value=transform_value(request))
    session.add(payload)
    session.commit()
    return payload.to_dict()


def transform_value(request: request.PayloadRequest):
    return ", ".join(request.list_1 + request.list_2).upper()


def get_payload(session: Session, payload_id: int, use_cache: bool = True):
    if use_cache:
        cached_payload = redis_client.get(f"payload_{payload_id}")
        if cached_payload:
            return json.loads(cached_payload)

    payload = (
        session.query(orm.PayloadData).filter(orm.PayloadData.id == payload_id).first()
    )
    session.close()

    if payload:
        redis_client.setex(
            f"payload_{payload_id}",
            int(os.getenv("REDIS_EXPIRE_TIME", 600)),
            json.dumps(payload.to_dict()),
        )
        return payload.to_dict()
