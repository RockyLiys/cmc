#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.contrib.auth.models import User, Group
from rest_framework import serializers, viewsets

from mysite.cmdb.models import ControlCp, ControlCpUrl


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:user-detail")

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff', 'date_joined')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:group-detail")

    class Meta:
        model = Group
        fields = ('url', 'name')


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    """
    允许查看和编辑user的 API endpoint
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    允许查看和编辑group的 API endpoint
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ControlCpUrlSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:controlcpurl-detail")

    class Meta:
        model = ControlCpUrl
        fields = ('url','host','in_url', 'out_url', 'create_time')

class ControlCpUrlViewSet(viewsets.ModelViewSet):
    """
    允许查看ControlCpUrl的 API endpoint

    """
    queryset = ControlCpUrl.objects.all()
    serializer_class = ControlCpUrlSerializer