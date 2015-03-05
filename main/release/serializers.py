# -*- coding: utf-8 -*-
from django.db import models
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from .models import Release


class ReleaseSerializer(serializers.ModelSerializer):
    class Meta():
        model = Release
