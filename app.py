import uvicorn

from fastapi import FastAPI
from database import dependencies, orm
from service import service
from domain import request, response

app = FastAPI(title="Cache Service", docs_url="/v1/docs")

orm.Base.metadata.create_all(bind=dependencies.engine)


@app.post("/payload", response_model=response.AddPayloadResponse, status_code=201)
def create_payload(request: request.PayloadRequest):
    db_session = dependencies.SessionLocal()
    payload = service.add_payload(db_session, request)
    resp = response.AddPayloadResponse(
        data=payload,
        status=201,
        message="Payload added successfully",
    )
    return resp


@app.get(
    "/payload/{payload_id}", response_model=response.GetPayloadResponse, status_code=200
)
def read_payload(payload_id: str):
    db_session = dependencies.SessionLocal()
    payload = service.get_payload(db_session, payload_id)
    resp = response.GetPayloadResponse(
        data=payload,
        status=200,
        message="Payload retrieved successfully",
    )
    return resp


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
