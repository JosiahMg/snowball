# 基础镜像为python3.8
FROM python:3.8
# 使用root用户
#USER root
# 设置为国内apt源
RUN sed -i s@/archive\.ubuntu\.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN sed -i s@/security\.ubuntu\.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN sed -i s@/cn\.archive\.ubuntu\.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
# 更新apt
RUN apt-get update
RUN apt-get install -y gcc g++
RUN apt-get install -y vim

# 在镜像中创建目录，用来存放本机中的django项目
RUN mkdir /usr/src/app
# 将本机 . 也就是当前目录下所有文件都拷贝到image文件中指定目录
COPY . /usr/src/app/
# 将/usr/src/app指定为工作目录
WORKDIR /usr/src/app/

RUN pip install --upgrade pip --index-url https://pypi.doubanio.com/simple/
# 在image中安装运行django项目所需要的依赖
RUN pip install -i https://pypi.doubanio.com/simple/ -r requirements.txt

# 开放容器的8080端口，允许外部链接这个端口
EXPOSE 8000

# 启动命令
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

RUN chmod u+x ./scripts/start.sh
CMD ["sh", "./scripts/start.sh"]