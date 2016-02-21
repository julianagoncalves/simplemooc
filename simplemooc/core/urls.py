#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf.urls import url


urlpatterns = [
    url(r'^$', 'simplemooc.core.views.home', name='home'),
    url(r'^contato/$', 'simplemooc.core.views.contact', name='contact'),
]
