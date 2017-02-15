from django.contrib.admin.sites import  AdminSite
from django.contrib import admin
from . import settings
class ContomSite(AdminSite):
	site_title = settings.ADMIN_NAME	
	site_header = settings.ADMIN_NAME

	site_url = settings.SITE_URL


admin.site = ContomSite()
print('===admin.site===')