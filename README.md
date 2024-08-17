# FastAPI Microservice Caching service


## API Endpoints

1. `POST /payload`: Create payload
2. `GET /payload/:payload_id`: Read generated payload by ID


## Tech Stack, Frameworks & Authentication

- Python with FastAPI framework
- PostgreSQL database with Alembic migration for database management
- Docker for containerization with Docker Compose for multiple containers
- Redis for in-memory caching system to speeding up reading performance


## How to run

1.  Start the service by running below command:
    ```
    sudo docker compose up
    ```


## How to test

1. When the service starts, the tests are already run before application deployment to ensure everything works correctly, so manual pytest execution is not necessary.
2. For convenience, if manual testing feels needed, start the service first, then access http://0.0.0.0:8000/v1/docs for Swagger API testing.


## Database Schema

```
class PayloadData(Base):
    __tablename__ = "payload_data"

    id = Column(String, primary_key=True, default=generate_uuid)
    value = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
```
