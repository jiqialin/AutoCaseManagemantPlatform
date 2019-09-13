"""AutoCaseInfoManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Auto Case Info Management APIs')


urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'docs/', schema_view),
    path(r'index/', include('index.urls'), name='index'),
    path(r'group/', include('group.urls')),
    path(r'caseInfo/', include('caseInfo.urls')),
    path(r'configuration/', include('configuration.urls')),
]