import datetime
import json


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime("%Y-%m-%common %H:%M:%S")
        # if isinstance(obj, bytes):
        #     return str(obj)
        else:
            return json.JSONEncoder.default(self, obj)
