#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _



class LogsConfig(AppConfig):
    name = 'mysite.logs'
    verbose_name = '日志'
