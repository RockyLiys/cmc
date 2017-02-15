# -*- coding: utf-8  -*-
#!/usr/local/bin/python

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from common.models import BaseModel

# Create your models here.

class ControlCp(BaseModel):
	remark = models.TextField('备注', max_length=1000)

	class Meta:
		db_table = 'cmc_cp'
		verbose_name = 'CP管理'
		verbose_name_plural = verbose_name	

class ControlCpUrl(BaseModel):
	host = models.CharField('HOST', max_length=100)
	in_url = models.CharField('接入URI', max_length=255)
	out_url = models.CharField('接出URI', max_length=255)
	remark = models.TextField('备注', max_length=1000)

	class Meta:
		db_table = 'cmc_cp_url'
		verbose_name = '配置CP地址'
		verbose_name_plural = verbose_name




