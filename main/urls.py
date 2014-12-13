from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'main.views.front_page', name='front_page'),
    url(r'^projects/', include('main.project.urls', namespace='project')),
    url(r'^tasks/', include('main.task.urls', namespace='task')),
    url(r'^accounts/', include('main.account.urls', namespace='account')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
)
