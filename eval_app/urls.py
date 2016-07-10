#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django.conf.urls import url

from . import views

urlpatterns = [
    # /eval_app
    url(r'^$', views.index, name='index'),
    # /eval_app/points
    url(r'^points/$', views.points, name='points'),
    url(r'^points/(?P<employee_name>[a-z]+)/', views.indexx, name='pointss'),



]

"""



"""