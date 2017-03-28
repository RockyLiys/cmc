from django.contrib import admin

# Register your models here.

from .models import Logs


@admin.register(Logs)
class LogsAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'control_cp_url', 'remark')
    search_fields = ('user__username', 'action')
    fieldsets = (
          ('User info', {
              'fields': ('user',)
          }),
          ('other info', {
              'fields': ('action','control_cp_url', 'remark')
          }),
    )


@admin.register(admin.models.LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    pass
