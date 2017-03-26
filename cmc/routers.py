# -*- coding: utf-8  -*-
# !/usr/local/bin/python
from __future__ import unicode_literals

from rest_framework import routers
from django.conf.urls import url
from collections import OrderedDict, namedtuple

from api.views import UserViewSet, GroupViewSet

from rest_framework import exceptions, renderers, views
from rest_framework.compat import NoReverseMatch
from rest_framework.renderers import BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.schemas import SchemaGenerator
from rest_framework.settings import api_settings
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.urls import urlpatterns as rf_urlpatterns


class DefaultRouter(routers.DefaultRouter):
    def __init__(self, *args, **kwargs):
        super(DefaultRouter, self).__init__(*args, **kwargs)

    def get_api_root_view(self, api_urls=None):
        """
        Return a basic root view.
        """
        api_root_dict = OrderedDict()
        list_name = self.routes[0].name
        for prefix, viewset, basename in self.registry:
            api_root_dict[prefix] = list_name.format(basename=basename)

        print('api_url.............')

        class APIRootView(views.APIView):
            _ignore_model_permissions = False
            exclude_from_schema = True

            def get(self, request, *args, **kwargs):
                # Return a plain {"name": "hyperlink"} response.
                ret = OrderedDict()
                print(dir(request))
                print(request.user)
                namespace = request.resolver_match.namespace
                print(namespace)
                for key, url_name in api_root_dict.items():
                    if namespace:
                        url_name = namespace + ':' + url_name
                    try:
                        ret[key] = reverse(
                            url_name,
                            args=args,
                            kwargs=kwargs,
                            request=request,
                            format=kwargs.get('format', None)
                        )
                    except NoReverseMatch:
                        # Don't bail out if eg. no list routes exist, only detail routes.
                        continue

                return Response(ret)

        return APIRootView.as_view()

    def get_urls(self):
        self.root_view_name = "cmc_api"
        self.include_root_view = True
        self.include_format_suffixes = True
        urls = super(DefaultRouter, self).get_urls()
        urls.extend(rf_urlpatterns)
        return urls


router = DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

for url in router.urls:
    print(url)
