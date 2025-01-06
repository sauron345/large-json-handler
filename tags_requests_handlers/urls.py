from django.urls import path

from tags_requests_handlers.error_handler import error_handler
from tags_requests_handlers.ip_tags_report_request_handler import IpTagsReportRequestHandler
from tags_requests_handlers.ip_tags_request_handler import IpTagsRequestHandler

urlpatterns = [
    path("ip-tags/<str:ip>", IpTagsRequestHandler.as_view(), name="ip-tags-list"),
    path("ip-tags-report/<str:ip>", IpTagsReportRequestHandler.as_view(), name="ip-report"),
]

handler404 = error_handler.page_not_found
handler500 = error_handler.internal_server
handler403 = error_handler.forbidden
handler400 = error_handler.bad_request
