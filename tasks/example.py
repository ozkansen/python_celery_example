from celery import Task

from main import app


class ExampleTask(Task):
    def run(self, *args, **kwargs):
        pass


app.register_task(ExampleTask)
