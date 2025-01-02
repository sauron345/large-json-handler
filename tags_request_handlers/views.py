import json

from django.http import HttpResponse
from django.views import View

from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response

from abc import ABC, abstractmethod

from tags_request_handlers.knowledge_base_handler import KnowledgeBaseHandler


class RequestHandler(View, ABC):

    @abstractmethod
    def get(self, request, ip, *args, **kwargs):
        knowledge_base_handler = KnowledgeBaseHandler()
        ip_tags = knowledge_base_handler.get_tags_by(ip)
        return ip_tags


class IpTagsRequestHandler(RequestHandler):

    def get(self, request, ip, *args, **kwargs):
        ip_tags = super().get(request, ip, *args, **kwargs)

        # if ip_tags:
        print(ip_tags)
        return HttpResponse({'tags': ip_tags}, status=status.HTTP_200_OK)

        # return render(request, self._TEMPLATE_NAME, {'error': "Invalid request"})


class IpTagsReportRequestHandler(RequestHandler):

    _TEMPLATE_NAME = "ip-tags-report.html"

    def get(self, request, ip, *args, **kwargs):
        ip_tags = super().get(request, ip, *args, **kwargs)

        return render(request, self._TEMPLATE_NAME, {'ip': ip, 'tags': ip_tags})

        # return render(request, self._TEMPLATE_NAME, {'error': "Invalid request"})
