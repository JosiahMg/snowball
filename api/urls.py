from django.urls import path
from django.http import HttpResponse
from api.views.stock_list import get_stocks


def index(request):
    return HttpResponse("Hello, world. You're at SnowBall.")


urlpatterns = [
    path('', index, name='index'),
    # 下载成分股
    path('query', get_stocks),
]
