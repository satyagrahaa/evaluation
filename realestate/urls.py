#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.real_estate_index, name='real_estate_index')
]