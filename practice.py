from celery import Celery
from celery.schedules import crontab
#celery -A practice worker -B -l INFO

# Create the Celery app
celery_app = Celery('tasks', broker="redis://localhost:6379", timezone='Asia/Calcutta')

@celery_app.task
def check():
    print("I am checking your stuff")
    # You can use logger.info instead of print for consistent logging

# Configure the Celery beat schedule
celery_app.conf.beat_schedule = {
    "run-me-every-ten-seconds": {
        "task": "practice.check",
        # "schedule": 10.0,
        "schedule": crontab(minute="*")
    }
}
