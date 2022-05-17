celery -A celery_tasks.main worker -l info -f logs/snowball_celery.log &
gunicorn -c gunicorn_config.py server.wsgi