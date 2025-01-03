from django.views import View
from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from abc import ABC, abstractmethod

from tags_request_handlers.error_handler import ErrorHandler
from tags_request_handlers.ip_address_validator import IpAddressValidator
from tags_request_handlers.knowledge_base_handler import KnowledgeBaseHandler


class RequestHandler(View, ABC):

    @abstractmethod
    def get(self, request, ip, *args, **kwargs):
        ip_tags = None
        ip_address_validator = IpAddressValidator(ip)
        if ip_address_validator.is_correct():
            knowledge_base_handler = KnowledgeBaseHandler()
            ip_tags = knowledge_base_handler.get_sorted_tags_by(ip)

        return ip_tags


class IpTagsRequestHandler(RequestHandler, APIView):

    def get(self, request, ip, *args, **kwargs):
        ip_tags = super().get(request, ip, *args, **kwargs)
        if ip_tags is not None:
            return Response(ip_tags, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid ip structure'}, status=status.HTTP_400_BAD_REQUEST)


class IpTagsReportRequestHandler(RequestHandler):

    _TEMPLATE_NAME = "ip-tags-report.html"

    def get(self, request, ip, *args, **kwargs):
        ip_tags = super().get(request, ip, *args, **kwargs)
        if ip_tags is not None:
            return render(request, self._TEMPLATE_NAME, {'ip': ip, 'tags': ip_tags})

        return render(
            request,
            'error-message.html',
            {'message': 'Error 400 - Invalid ip structure', 'title': 'Bad Request'}
        )
