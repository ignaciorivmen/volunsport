from django.db import models
from django import forms
from django.contrib.auth.models import User

STATES = (
	('AC','ACCEPTED'),
	('DE','DENIED'),
	('AW','AWAITING'),
)

class Volunteer(models.Model):
	
	user = models.OneToOneField(User , unique=True)
	name = models.CharField(max_length=50)
	
	subcribedToOrganizer = models.ManyToManyField('Organizer', null=True)
	subcribedToEvent = models.ManyToManyField('EventVolunteer', null=True)
	sports = models.ManyToManyField('Sport', null=True)
	
	def __unicode__(self):
		return self.name

class Organizer(models.Model):
	
	user = models.OneToOneField(User , unique=True)
	name = models.CharField(max_length=50)
	eventsOrganized = models.ManyToManyField('Event', null=True, related_name='Organizers')
	sports = models.ManyToManyField('Sport')
	volunteersSubcribed = models.ManyToManyField('Volunteer', null=True) 

	def __unicode__(self):
		return self.name

class Event(models.Model):
	
	name = models.CharField(max_length=50)
	date = models.DateField()

	organizer = models.ForeignKey('Organizer')
	volunteers = models.ManyToManyField('EventVolunteer', null=True, related_name='Events')
	sports = models.ManyToManyField('Sport')

	def __unicode__(self):
		return self.name

class EventVolunteer(models.Model):
	
	state = models.CharField(max_length=10, choices=STATES)
	valuation = models.PositiveIntegerField(null=True)
	experience = models.CharField(max_length=256 , null=True)
	
	event = models.ForeignKey('Event')
	volunteers = models.ManyToManyField('Volunteer', null=True)

	def __unicode__(self):
		return self.state
		
class Sport (models.Model):
	
	name = models.CharField(max_length=50)
	
	organizers = models.ManyToManyField('Organizer', null=True)
	volunteers = models.ManyToManyField('Volunteer', null=True)
	events = models.ManyToManyField('Event', null=True)

	def __unicode__(self):
		return self.name

