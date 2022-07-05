# celery_template_worker

###### created by Weber Huang

```bash
$ git clone https://github.com/Weber12321/celery_template_worker.git

$ cd celery_template_worker
```

```bash
$ touch .env

$ vim .env

REDIS=redis://<ip>:6379/0
```

```bash
$ docker build -t ychuang/celery_app_1 --no-cache .

$ docker run --name celery_cluster_1 --env-file .env ychuang/celery_app_1

# now send a message from remote client see the result
```

