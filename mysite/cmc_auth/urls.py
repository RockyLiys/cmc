#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.conf.urls import include, url
from . import views

app_name = 'cmc_auth'
urlpatterns = [
    # Examples:
    url(r'^$', views.IndexView.as_view(), name='index'),
]