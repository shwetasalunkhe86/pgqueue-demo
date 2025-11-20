import json
import asyncpg
from pgqueuer import PgQueuer
from pgqueuer.db import AsyncpgDriver
from pgqueuer.models import Job
from app.service import execute_monitoring_service

async def main() -> PgQueuer:
    connection = await asyncpg.connect(
        host="localhost",
        port=5555,
        user="testrunner_queue",
        password="testrunner_queue",
        database="testrunner_queue",
    )
    driver = AsyncpgDriver(connection)
    pgq = PgQueuer(driver)

    @pgq.entrypoint("monitoring")
    async def handle_monitoring(job: Job) -> None:
        raw_payload = json.loads(job.payload.decode())
        payload = raw_payload.get("payload")

        result = await execute_monitoring_service(payload)
        print(result)

    return pgq