#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _



class LogsConfig(AppConfig):
    name = 'logs'
    verbose_name = '日志中心'
    label = verbose_name

    def ready(self):
        super(CmdbConfig, self).ready()
        self.module.autodiscover()
