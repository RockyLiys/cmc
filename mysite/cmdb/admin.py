# -*- coding: utf-8  -*-
# !/usr/local/bin/python

from django.contrib import admin
from django.contrib.admin import TabularInline, StackedInline

# Register your models here.

from .models import ControlCp, ControlCpUrl


class ControlCpInline(TabularInline):
    model = ControlCp.cp_urls.through
    extra = 0


@admin.register(ControlCp)
class ControlCpAdmin(admin.ModelAdmin):
    # inlines = (ControlCpInline,)

    empty_value_display = '-empty-'
    list_display = ('cp', 'cp_urls','create_time', 'update_time', 'remark')
    search_fields = ('cp__username',)
    fieldsets = (
          (None, {
              'fields': ('cp', 'cp_urls', 'remark')
          }),
    )
    def cp_urls(self, obj):
        print(obj)
        return obj.cp_urls


@admin.register(ControlCpUrl)
class ControlCpUrlAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('host', 'in_url', 'out_url', 'create_time', 'update_time', 'remark')
    search_fields = ('host',)
    fieldsets = (
        (None, {
            'fields': ('host', 'in_url', 'out_url', 'remark')
        }),
    )
