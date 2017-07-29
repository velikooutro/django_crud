# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from basic_app.models import School, Students

# Register your models here.
admin.site.register(School)
admin.site.register(Students)
