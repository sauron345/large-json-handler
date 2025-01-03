from django.urls import path

from tags_request_handlers.error_handler import ErrorHandler
from tags_request_handlers.request_handler import IpTagsRequestHandler, IpTagsReportRequestHandler


urlpatterns = [
    path("ip-tags/<str:ip>", IpTagsRequestHandler.as_view(), name="ip-tags-list"),
    path("ip-tags-report/<str:ip>", IpTagsReportRequestHandler.as_view(), name="ip-report"),
]

error_handler = ErrorHandler()

handler404 = error_handler.page_not_found
handler500 = error_handler.internal_server
handler403 = error_handler.forbidden
handler400 = error_handler.bad_request
