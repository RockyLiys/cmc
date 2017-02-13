#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.contrib.auth.models import User, Group
from rest_framework import serializers, viewsets
from rest_framework_xml.parsers import XMLParser
from rest_framework_xml.renderers import XMLRenderer

# Ser#!/usr/bin/env python
# -*- coding:utf-8 -*-

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    """
    允许查看和编辑user的 API endpoint
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    parser_classes = (XMLParser,)
    renderer_classes = (XMLRenderer,)



class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class GroupViewSet(viewsets.ModelViewSet):
    """
    允许查看和编辑group的 API endpoint
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer