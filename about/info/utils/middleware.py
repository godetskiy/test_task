#-*- coding:utf-8 -*-
from info.models import LogRequest


class RequestWare:
    def process_request(self, request):
        req = LogRequest(
            host = request.get_host(),
            path = request.get_full_path(),
            method = request.method
        )
        req.save()
        return None
