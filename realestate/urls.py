from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.real_estate_index, name='real_estate_index')
]