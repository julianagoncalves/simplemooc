#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf.urls import url


urlpatterns = [
    url(r'^$', 'simplemooc.courses.views.index', name="index"),
]
