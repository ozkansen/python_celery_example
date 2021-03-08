from celery import Celery

app = Celery("tasks", broker="redis://127.0.0.1:6379/0")

app.conf.update(
    timezone="Europe/Istanbul",
    enable_utc=True,
    include=["tasks"],
    beat_schedule={"example": {"task": "tasks.example.ExampleTask", "schedule": 5}},
)
