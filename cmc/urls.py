#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""cmc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from cmc import settings
from cmc.routers import router
from . import views

admin.site.site_title = settings.ADMIN_NAME
admin.site.site_header = settings.ADMIN_NAME

admin.site.site_url = settings.SITE_URL

urlpatterns = [
    # Examples:
    url(r'^$', views.home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns += [
    url(r'^api/', include(router.urls, namespace='api', app_name='api')),
    # url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

print("cmc_urls.................")
for url in urlpatterns:
    print(url)


