import sys
# 代理人：指定redis作为消息队列

if sys.platform.startswith('win'):
    broker_url = 'redis://127.0.0.1:6379/9'
    result_backend = "redis://127.0.0.1:6379/10"
else:
    broker_url = 'redis://topo_manage_redis:6379/9'
    result_backend = "redis://topo_manage_redis:6379/10"
timezone = "Asia/Shanghai"
enable_utc = False
worker_concurrency = 10

# backend result保存3天
# result_expires = 60*60*24*3
result_expires = 60*60
