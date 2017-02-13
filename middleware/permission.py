#!/usr/local/bin/python
# -*- coding: utf-8 -*-

try:
    from django.utils.deprecation import MiddlewareMixin  # Django 1.10.x
except ImportError:
    MiddlewareMixin = object  # Django 1.4.x - Django 1.9.x

class CoreMiddleware(MiddlewareMixin):

    def process_request(self, request):
        pass

    def process_response(self, request, response):
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
        response["has_permission"] = True
        print('sssssssssssss')
        print(request)
        print(response)
        return response
