from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from tags_requests_handlers.request_handler import RequestHandler


class IpTagsRequestHandler(RequestHandler, APIView):

    def get(self, request, ip, *args, **kwargs):
        ip_tags = super().get(request, ip, *args, **kwargs)
        if ip_tags is not None:
            return Response(ip_tags, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid ip structure'}, status=status.HTTP_400_BAD_REQUEST)
