# Snow Ball

## 功能描述
The snowball grew bigger and bigger

## window启动方法
python manage.py runserver  
celery -A celery_tasks.main worker -l info -P eventlet

## 生产环境 ubuntu启动方法
docker-compose up -d


## 配置文件说明
start.sh: 启动django服务  
.env: 配置镜像版本TAG

## TODO
1. 上证50 中证500 中证红利成分股
2. 低估值的股票池
3. 成长性好的基金