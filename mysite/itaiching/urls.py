from django.conf.urls import url

from . import views

app_name = 'itaiching'
urlpatterns = [
    url(r'^$', views.style13, name='style13'),
    url(r'^style13/', views.style13, name='style13'),
    url(r'^style19/', views.style19, name='style19'),


]
