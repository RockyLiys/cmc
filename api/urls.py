# -*- coding: utf-8  -*-
#!/usr/local/bin/python
from __future__ import unicode_literals

from rest_framework import routers
from django.conf.urls import url
from .views import UserViewSet, GroupViewSet

class DefaultRouter(routers.DefaultRouter):

    def get_urls(self):
        self.root_view_name = "cmc_api"
        urls = super(DefaultRouter, self).get_urls()
        print('fffffffffffsssssssssssss')
        print(dir(self))
        print(self.root_view_name)
        # root_url = url(r'^cmc$', self.get_api_root_view(api_urls=urls), name=self.root_view_name)
        # urls.append(root_url)

        for url in urls:
            print(url)
        return urls

router = DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
