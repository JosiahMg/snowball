from django.urls import path
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at SnowBall.")


urlpatterns = [
    path('', index, name='index'),
    # 请求答案
    # path('query', project_list.get_project_list),  # 请求答案



]