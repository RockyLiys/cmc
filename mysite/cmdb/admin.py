# -*- coding: utf-8  -*-
#!/usr/local/bin/python

from django.contrib import admin


# Register your models here.

from .models import ControlCp, ControlCpUrl

@admin.register(ControlCp)
class ControlCpAdmin(admin.ModelAdmin):
	pass

@admin.register(ControlCpUrl)
class ControlCpUrlAdmin(admin.ModelAdmin):
	pass
