from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from typing import List
from celery.result import AsyncResult

from main import Appium_class

from queue_modul import run_appium_test_queue




class TestRequest(BaseModel):
    hotel_name: str
    date_list: List[List[int]]


app = FastAPI()

@app.post("/appium_test_runner")
async def dynamic(hotel_data: TestRequest):
    hotel_name = hotel_data.hotel_name
    date_list = hotel_data.date_list

    appium_test_runner = Appium_class(hotel_name, date_list)

    result = appium_test_runner.test_get_info()

    return result


@app.post("/appium_test_runner_queue")
async def send_task(hotel_data: TestRequest):
    hotel_name = hotel_data.hotel_name
    date_list = hotel_data.date_list

    task = run_appium_test_queue.delay(hotel_name, date_list)
    return {"task_id": task.id}


@app.get("/task_status/{task_id}")
async def get_task_status(task_id: str):
    task_result = AsyncResult(task_id)

    if task_result.state == "PENDING":
        return {"task_id": task_id, "status": "pending"}
    elif task_result.state == "SUCCESS":
        return {"task_id": task_id, "status": "completed", "result": task_result.result}
    elif task_result.state == "FAILURE":
        return {"task_id": task_id, "status": "failed", "error": str(task_result.info)}

    return {"task_id": task_id, "status": task_result.state}


if __name__ == '__main__':
    uvicorn.run('rest_api:app', host="127.0.0.1", port=8000, reload=True)