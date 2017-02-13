from django.contrib.admin.sites import site, AdminSite
from . import settings
class AdminSite(AdminSite):
	site_title = settings.ADMIN_NAME	
	site_header = settings.ADMIN_NAME

	site_url = settings.SITE_URL

site = AdminSite()