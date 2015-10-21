from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login', views.login_view, name='login'),
    url(r'^logout', views.logout_view, name='logout'),
    url(r'^authenticate$', views.authenticate_view, name='authenticate'),
    url(r'^(?P<pk>[0-9]+)/$', views.detail, name='detail'),
]
