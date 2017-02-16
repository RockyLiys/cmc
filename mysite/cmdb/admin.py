# -*- coding: utf-8  -*-
#!/usr/local/bin/python

from django.contrib import admin


# Register your models here.

from .models import ControlCp, ControlCpUrl

@admin.register(ControlCp)
class ControlCpAdmin(admin.ModelAdmin):
	empty_value_display = '-empty-'
	list_display = ('cp', 'create_time', 'update_time', 'remark')

@admin.register(ControlCpUrl)
class ControlCpUrlAdmin(admin.ModelAdmin):
	empty_value_display = '-empty-'
	list_display = ('host', 'in_url', 'out_url', 'create_time', 'update_time')
