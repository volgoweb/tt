# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from .views import Login


urlpatterns = patterns('',
    url(r'^login/$', Login.as_view(), name='login'),
    #url(r'^(?P<slug>[^/]+)/$', 'main.portfolio.views.portfolio_detail_page', name='portfolio__portfolio_detail_page'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': 'front_page'}, name='logout'),
)
