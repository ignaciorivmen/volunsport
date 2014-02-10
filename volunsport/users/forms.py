from django import forms
from users.models import *

class VolunteerForm(ModelForm):
	class Meta:
		model = Volunteer
		fields = ['user', 'name', 'subcribedToOrganizer', 'subcribedToEvent', 'sports']

class OrganizerForm(ModelForm):
	class Meta:
		model = Organizer
		fields = ['user', 'name', 'eventsOrganized', 'sports', 'volunteersSubcribed']

class EventForm(ModelForm):
	class Meta:
		model = Event
		fields = ['name', 'date', 'organizer', 'volunteers', 'sports']

class EventVolunteerForm(ModelForm):
	class Meta:
		model = EventVolunteer
		fields = ['state', 'valuation', 'experience', 'event', 'volunteers']

class SportForm(ModelForm):
	class Meta:
		model = Sport
		fields = ['name', 'organizers', 'volunteers', 'events']
