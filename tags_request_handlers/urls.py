from django.urls import path
from .views import IpTagsRequestHandler, IpTagsReportRequestHandler

urlpatterns = [
    path("ip-tags/<str:ip>", IpTagsRequestHandler.as_view(), name="ip-tags-list"),
    path("ip-tags-report/<str:ip>", IpTagsReportRequestHandler.as_view(), name="ip-report"),
]
