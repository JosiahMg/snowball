"""
使用facebook pysparnn训练模型
"""
import sys
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from api.views.common.date_encoder import DateEncoder
from api.views.common.status import Status, INIT_STATUS, STATUS
from common.space_monitor import space_ratio_warning
from common.log_utils import get_logger

logger = get_logger(__name__)


def post_method_proc(request, context):
    try:
        params_dict = request.POST
        if request.content_type == 'application/json':
            params_dict = json.loads(request.body if request.body else '{}')
        pass

    except Exception as e:
        message = '显示信息失败:{}'.format(e)
        logger.error(message, exc_info=False)
        STATUS[Status.OTHER_ERROR.name]['message'] = message
        context.update(STATUS[Status.OTHER_ERROR.name])

    return HttpResponse(json.dumps(context, cls=DateEncoder, ensure_ascii=False),
                        content_type="application/json; charset=utf-8")


def other_method_proc(request, context):
    logger.debug('get method request')
    context.update(STATUS[Status.BAD_GET.name])
    return HttpResponse(json.dumps(context, cls=DateEncoder, ensure_ascii=False),
                        content_type="application/json; charset=utf-8")


@csrf_exempt
def get_sh50(request):
    context = INIT_STATUS.copy()
    if request.method == 'POST':
        return post_method_proc(request, context)
    else:
        return other_method_proc(request, context)
