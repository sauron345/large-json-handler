from django.views import View

from abc import ABC, abstractmethod

from large_json_handler.startup import knowledge_base_sorted_handler


class RequestHandler(View, ABC):

    @abstractmethod
    def get(self, request, ip, *args, **kwargs):
        ip_tags = knowledge_base_sorted_handler.get_sorted_tags_by(ip)
        return ip_tags
