from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from resume.views import index, work,projects,skills,courses,home
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'personal_site.views.home', name='home'),
    # url(r'^personal_site/', include('personal_site.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',index),
    url(r'^work/', work),
    url(r'^home/',home),
    url(r'^courses/',courses),
    url(r'^projects/',projects),
    url(r'^skills/',skills),
    # static

)
urlpatterns += staticfiles_urlpatterns()

