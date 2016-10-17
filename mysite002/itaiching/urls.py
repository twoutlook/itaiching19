from django.conf.urls import url

from . import views

app_name = 'itaiching'
urlpatterns = [
    url(r'^$', views.style13, name='style13'),
    url(r'^style13/', views.style13, name='style13'),
    # url(r'^style19/', views.style19, name='style19'),這會觸發任何  style19/XXX
    url(r'^style19/$', views.style19, name='style19'),
    url(r'^style19/(?P<setnum>[0-9]+)/$', views.style19detail, name='style19detail'),
    url(r'^style19/(?P<setnum>[0-9]+)/(?P<movenum>[0-9]+)', views.style19detail2, name='style19detail2'),
    # url(r'^route38/(?P<setnum>[0-9]+)/(?P<movenum>[0-9]+)', views.route38move, name='route38move'),
    # url(r'^route38/(?P<setnum>[0-9]+)/(?P<movenum>[0-9]+)', views.route38move, name='route38move'),
    url(r'^route38/', views.route38, name='route38'),


]
