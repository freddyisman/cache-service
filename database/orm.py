from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from uuid import uuid4
from datetime import datetime

Base = declarative_base()


def generate_uuid():
    return str(uuid4())


class PayloadData(Base):
    __tablename__ = "payload_data"

    id = Column(String, primary_key=True, default=generate_uuid)
    value = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now)

    def to_dict(self):
        return {
            "id": self.id,
            "value": self.value,
        }
