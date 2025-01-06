from django.urls import path

from tags_requests_handlers.ip_tags_report_request_handler import IpTagsReportRequestHandler
from tags_requests_handlers.ip_tags_request_handler import IpTagsRequestHandler

urlpatterns = [
    path("ip-tags/<str:ip>", IpTagsRequestHandler.as_view(), name="ip-tags-list"),
    path("ip-tags-report/<str:ip>", IpTagsReportRequestHandler.as_view(), name="ip-report"),
]

