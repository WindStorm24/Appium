from celery import Celery
from main import Appium_class


celery_app = Celery(
    "tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)



@celery_app.task()
def run_appium_test_queue(hotel_name, date_list):

    appium_test_runner = Appium_class(hotel_name, date_list)
    result = appium_test_runner.test_get_info()
    return result



