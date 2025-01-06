from django.shortcuts import render

from tags_requests_handlers.request_handler import RequestHandler


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
