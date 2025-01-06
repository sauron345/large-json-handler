from django.shortcuts import render
from django.views import View

from tags_requests_handlers.singleton_meta import SingletonMeta


class ErrorHandler(View, metaclass=SingletonMeta):

    _TEMPLATE_NAME = 'error-message.html'

    def page_not_found(self, request):
        return render(
            request,
            self._TEMPLATE_NAME,
            {'message': '404 - Page not found', 'title': 'Page not found'}
        )

    def internal_server(self, request):
        return render(
            request,
            self._TEMPLATE_NAME,
            {'message': '500 - Internal server error', 'title': 'Internal Server Error'},
        )

    def forbidden(self, request):
        return render(
            request,
            self._TEMPLATE_NAME,
            {'message': '403 - Forbidden', 'title': 'Forbidden'}
        )

    def bad_request(self, request):
        return render(
            request,
            self._TEMPLATE_NAME,
            {'message': '400 - Bad request', 'title': 'Bad Request'}
        )


error_handler = ErrorHandler()
