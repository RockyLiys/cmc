# -*- coding: utf-8  -*-
#!/usr/local/bin/python

from django.contrib import admin


# Register your models here.

from .models import ControlCp, ControlCpUrl

class ControlCpAdmin(admin.ModelAdmin):
	pass

class ControlCpUrlAdmin(admin.ModelAdmin):
	pass

admin.site.register(ControlCp, ControlCpAdmin)
admin.site.register(ControlCpUrl, ControlCpUrlAdmin)


