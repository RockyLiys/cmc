# -*- coding: utf-8  -*-
# !/usr/local/bin/python

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User

from common.models import BaseModel


# Create your models here.


@python_2_unicode_compatible
class ControlCpUrl(BaseModel):
    host = models.CharField('HOST', max_length=100)
    in_url = models.CharField('接入URI', max_length=255)
    out_url = models.CharField('接出URI', max_length=255)

    def __str__(self):
        return self.host
        # '/'.join([self.host, self.in_url, self.out_url])

    class Meta:
        db_table = 'cmc_cp_url'
        verbose_name = '配置CP地址'
        verbose_name_plural = verbose_name


@python_2_unicode_compatible
class ControlCp(BaseModel):
    cp = models.ForeignKey(User, default=True, verbose_name='CP用户')
    cp_urls = models.ManyToManyField('ControlCpUrl', verbose_name='CP配置地址')

    def __str__(self):
        return self.cp.username

    class Meta:
        db_table = 'cmc_cp'
        verbose_name = 'CP管理'
        verbose_name_plural = verbose_name
