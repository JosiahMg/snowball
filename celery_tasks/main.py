from celery import Celery
import os
from datetime import timedelta

# 读取Django的配置，
os.environ["DJANGO_SETTINGS_MODULE"] = "server.settings"

# 创建celery对象，并指定配置
app = Celery("gis_celery_tasks")

# celery项目配置： worker代理人，指定任务存储到哪里区。
app.config_from_object('celery_tasks.config')

# 注册异步任务和定时任务
app.autodiscover_tasks([
    'celery_tasks.fillna',
    'celery_tasks.node_pipe_match',
    # 'celery_tasks.clear_files',
    'celery_tasks.check',
])

# 定时器任务
# celery -A celery_tasks.main beat
# app.conf.beat_schedule = {
#     'clear_db': {
#         'task': 'celery_tasks.clear_files.tasks.clear_files',
#         # 每隔n秒执行一次
#         # 'schedule': crontab(minute="*/1"),
#         'schedule': timedelta(seconds=6),
#         # 传递参数
#         # 'args': ("123",)
#     }
# }
