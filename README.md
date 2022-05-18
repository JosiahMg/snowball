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


# issue
1. ImportError: DLL load failed while importing win32api
anaconda环境的"Scripts" 文件夹下执行 "python  pywin32_postinstall.py  -install"


## TODO
1. 低估值的股票池
2. 成长性好的基金