import asyncio
import json

import asyncpg
from pgqueuer import AsyncpgDriver, Queries


async def schedule_job(payload: dict):
    connection = await asyncpg.connect(
        host="localhost",
        port=5555,
        user="testrunner_queue",
        password="testrunner_queue",
        database="testrunner_queue",
    )

    driver = AsyncpgDriver(connection)
    queue = Queries(driver)

    encoded_payload = json.dumps({
        "payload": payload
    }).encode()

    job_id = await queue.enqueue(
        entrypoint="monitoring",
        payload=encoded_payload,
    )
    print(f"Scheduled job {job_id} for run_id={payload["run_id"]}")
    await connection.close()


if __name__ == "__main__":
    asyncio.run(schedule_job(
        payload={"run_id": 1001, "duration": 60, "service_type": "monitoring", "panel_id":1, "variable":{"var1":"1", "var2":"2"}}
    ))