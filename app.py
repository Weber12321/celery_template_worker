import os

from celery import Celery

app = Celery(
    name='proj_A',
    broker=os.getenv('REDIS'),
    backend=os.getenv('REDIS')
)

app.conf.task_routes = {
    'A.*': {'queue': 'A_queue'},
    'B.*': {'queue': 'B_queue'},
}


@app.task
def sample_task(value):
    return f"{value} return from remote worker_1"
