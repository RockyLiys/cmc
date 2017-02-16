#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CmdbConfig(AppConfig):
    name = 'mysite.cmdb'
    verbose_name = '配置管理中心'
