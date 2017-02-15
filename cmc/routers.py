# -*- coding: utf-8  -*-
#!/usr/local/bin/python

from rest_framework import routers



class DefaultRouter(routers.DefaultRouter):
	def get_urls(self):
		urls = super(DefaultRouter, self).get_urls()
		print(urls)
		print('fffffffffffsssssssssssss')
		return urls
