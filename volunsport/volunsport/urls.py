from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'volunsport.views.home', name='home'),
    # url(r'^volunsport/', include('volunsport.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),

    url(r'^$', 'users.views.index',name="index"),
    url(r'^about/$', 'users.views.about',name="about"),
    url(r'^notices/$', 'users.views.notices',name="notices"),
    url(r'^resources/$', 'users.views.resources',name="resources"),
    url(r'^register/$', 'users.views.register',name="register"),
    

    url(r'^accounts/login/$', "django.contrib.auth.views.login", name="login"),

    url(r'^volunteers/$', 'users.views.volunteers_index'),
    url(r'^volunteers/(?P<volunteer_id>\d+)/$', 'users.views.volunteer_details', name='volprofile'),
    url(r'^volunteers/(?P<volunteer_id>\d+)/events_before/$', 'users.views.volunteer_events_before', name = 'nexteve'),
    url(r'^volunteers/(?P<volunteer_id>\d+)/events_after/$', 'users.views.volunteer_events_after', name='fineve'),
    url(r'^volunteers/(?P<volunteer_id>\d+)/experiences/$', 'users.views.volunteer_exp', name='expvol'),

    url(r'^organizers/$', 'users.views.organizers_index'),
    url(r'^organizers/(?P<organizer_id>\d+)/$', 'users.views.organizer_details', name = 'orgprofile'),
    url(r'^organizers/(?P<organizer_id>\d+)/events_before/$', 'users.views.organizer_events_before', name= 'orgnexteve'),
    url(r'^organizers/(?P<organizer_id>\d+)/events_after/$', 'users.views.organizer_events_after', name= 'orgfineve'),

    url(r'^events/$', 'users.views.events_index',name="events"),
    url(r'^events/(?P<event_id>\d+)/$', 'users.views.event_details'),

    url(r'^experiences/$', 'users.views.experience_index',name="experiences"),
    url(r'^experiences/(?P<exp_id>\d+)/$', 'users.views.experience_details'),

    url(r'^volunteerreg/$', 'users.views.volunteer_register', name='regvol'),
    url(r'^organizerreg/$', 'users.views.organizer_register', name='regorg'),
    url(r'^eventreg/$', 'users.views.event_register', name='regeve'),
    url(r'^register/$', 'users.views.register'),
    url(r'^eventvolregister/$', 'users.views.event_volunteer_register'),
    url(r'^selectregister/$', 'users.views.selectregister', name='selectregister'),
)

#urlpatterns += patterns('',
#    url(r'^admin/', include(admin.site.urls)),
#)
