# -*- coding: utf-8  -*-
#!/usr/local/bin/python

from django.db import models
from django.contrib.auth.models import User
from common.models import BaseModel
from django.utils.encoding import python_2_unicode_compatible

from mysite.cmdb.models import ControlCpUrl

# Create your models here.

@python_2_unicode_compatible
class Logs(BaseModel):
	user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=True)
	control_cp_url = models.ForeignKey(ControlCpUrl, on_delete=models.SET_DEFAULT, default=True)
	remark = models.TextField('备注', max_length=1000)

	class Meta:
		db_table = 'cmc_logs'
		verbose_name = '日志'
		verbose_name_plural = verbose_name
