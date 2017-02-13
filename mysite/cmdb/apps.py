#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CmdbConfig(AppConfig):
    name = 'cmdb'
    verbose_name = _'配置管理中心'

    
    def ready(self):
        super(CmdbConfig, self).ready()
        self.module.autodiscover()
