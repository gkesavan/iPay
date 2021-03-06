from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('ipay_dashboard.views',
    url(r'^$', 'dashboard', name='dashboard'),
    url(r'^create/$', 'create_payment', name='create_payment'),
)
