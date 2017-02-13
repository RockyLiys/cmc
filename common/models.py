# -*- coding: utf-8  -*-
#!/usr/local/bin/python

from django.db import models

# Create your models here.

class BaseModel(models.Model):
	create_time = models.DateTimeField('创建时间', auto_now_add=True)
	update_time = models.DateTimeField('更新时间', auto_now=True)

	class Meta:
		abstract = True

	def __str__(self):
		return str(self.pk)
