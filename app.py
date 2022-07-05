import os

from dotenv import load_dotenv
from celery import Celery

load_dotenv('.env')

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
    print(value, "worker_1", "183")
