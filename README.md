# FastAPI Microservice Caching service


## API Endpoints

1. `POST /payload`: Create payload
2. `GET /payload/:payload_id`: Read generated payload by ID


## Tech Stack, Frameworks & Authentication

- Python with FastAPI framework
- PostgreSQL database with Alembic migration for database management
- Docker for containerization with Docker Compose for multiple containers


## How to run

1. Set up environment variables:
   - Create a `.env` file.
   - Add the necessary environment variables details following example of `.env.sample` file.

2. (Optional) For testing run following command:
   ```
   poetry run pytest test
   ```
   Notes: for integration testing, adjust `LOCALHOST_DATABASE_URL` variable in `test/integration/test_service.py` with localhost database configuration

3. Start the service by running below command:
   ```
   sudo docker compose up
   ```

## Database Schema

```
class PayloadData(Base):
    __tablename__ = "payload_data"

    id = Column(String, primary_key=True, default=generate_uuid)
    value = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
```