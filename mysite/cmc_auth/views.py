#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.generic import TemplateView


class IndexView(TemplateView):
	template_name = 'auth.html'

