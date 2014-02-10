from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'volunsport.views.home', name='home'),
    # url(r'^volunsport/', include('volunsport.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    
	url(r'^volunteers/$', 'users.views.volunteersIndex'),
	url(r'^volunteers/(?P<volunteer_id>\d+)/$', 'users.views.volunteerDetails'),
	url(r'^organizers/$', 'users.views.organizersIndex'),
	url(r'^organizers/(?P<organizer_id>\d+)/$', 'users.views.organizerDetails'),
	url(r'^events/$', 'users.views.eventsIndex'),
	url(r'^events/(?P<event_id>\d+)/$', 'users.views.eventDetails'),
	url(r'^sports/$', 'users.views.sportsIndex'),
	url(r'^sports/(?P<sport_id>\d+)/$', 'users.views.sportDetails'),
	url(r'^eventVolunteers/$', 'users.views.eventVolunteersIndex'),
	url(r'^eventVolunteers/(?P<eventVolunteer_id>\d+)/$', 'users.views.eventVolunteerDetails'),
    
    
)
