from django.shortcuts import render
from django.views import View

from recruitment_task_nask.singleton_meta import SingletonMeta


class ErrorsHandler(View, metaclass=SingletonMeta):

    _TEMPLATE_NAME = 'error-message.html'

    def page_not_found(self, request, exception):
        return render(
            request,
            self._TEMPLATE_NAME,
            {'message': '404 - Page not found', 'title': 'Page not found'},
            status=404
        )

    def internal_server(self, request):
        return render(
            request,
            self._TEMPLATE_NAME,
            {'message': '500 - Internal server error', 'title': 'Internal Server Error'},
            status=500
        )

    def forbidden(self, request, exception):
        return render(
            request,
            self._TEMPLATE_NAME,
            {'message': '403 - Forbidden', 'title': 'Forbidden'},
            status=403
        )

    def bad_request(self, request, exception):
        return render(
            request,
            self._TEMPLATE_NAME,
            {'message': '400 - Bad request', 'title': 'Bad Request'},
            status=400
        )


error_handler = ErrorsHandler()
