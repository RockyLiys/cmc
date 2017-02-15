from django.contrib import admin

# Register your models here.

from .models import Logs


@admin.register(Logs)
class LogsAdmin(admin.ModelAdmin):
	pass

@admin.register(admin.models.LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
	pass
