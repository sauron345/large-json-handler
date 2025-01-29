"""
URL configuration for large_json_handler project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include

from large_json_handler.errors_handler import error_handler

urlpatterns = [
    path('', include('tags_requests_handlers.urls')),
]

handler404 = error_handler.page_not_found
handler500 = error_handler.internal_server
handler403 = error_handler.forbidden
handler400 = error_handler.bad_request
