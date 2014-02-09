"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from users.models import *
from django.contrib.auth.models import User
from MySQLdb import ProgrammingError, IntegrityError
import datetime


class VolunteerTest(TestCase):

	def create_volunteer_userNull(self):
		name = "Volunteer1"
		return Volunteer.objects.create(name=name)
		
	def test_Volunteer_userNull(self):
		self.assertRaises(Exception, self.create_volunteer_userNull)

	def create_volunteer(self, name):
		user = User.objects.create(username='Volunteer1', email='Volunteer1@email.com')
		vol = Volunteer(name=name, user = user)
		vol.save()
		return vol

	def test_Volunteer_nameShort(self):
		vol = self.create_volunteer("Volunteer1")
		
		self.assertTrue(isinstance(vol, Volunteer))
		self.assertEqual(vol.__unicode__(), vol.name)

	def test_Volunteer_nameLong(self):
		self.assertRaises(Warning, self.create_volunteer, "this is a really long name , this is a really long name")
		
	def test_Volunteer_nameNull(self):
		self.assertRaises(Exception, self.create_volunteer, None)
		
	def test_Volunteer_orgNotNull(self):
		vol = self.create_volunteer("Volunteer1")
		userOrg = User.objects.create(username='Organizer1', email='organizer1@email.com')
		sport = Sport.objects.create(name = 'sport1')
		org = Organizer.objects.create(name = 'Organizer1', user = userOrg)
		org.sports.add(sport)
		vol.subcribedToOrganizer.add(org)
		
		self.assertTrue(isinstance(vol, Volunteer))
	
		
	def test_Volunteer_sportNotNull(self):
		vol = self.create_volunteer("Volunteer1")
		sport = Sport.objects.create(name = 'sport1')
		vol.sports.add(sport)		
		
		self.assertTrue(isinstance(vol, Volunteer))
		
	def test_Volunteer_eventNotNull(self):
		vol = self.create_volunteer("Volunteer1")
		userOrg = User.objects.create(username='Organizer1', email='organizer1@email.com')
		sport = Sport.objects.create(name = 'sport1')
		org = Organizer.objects.create(name = 'Organizer1', user = userOrg)
		org.sports.add(sport)
		ev = Event.objects.create(name="event1", date=datetime.date(2010, 1, 1), organizer=org)
		ev.sports.add(sport) 
		eventvol = EventVolunteer(state="ACCEPTED", valuation=2, experience="good" , event=ev)
		eventvol.save()
		
		self.assertTrue(isinstance(vol, Volunteer))
		
class OrganizerTest(TestCase):

	def create_Organizer_userNull(self):
		name = "Organizer1"
		return Organizer.objects.create(name=name)
		
	def test_Organizer_userNull(self):
		self.assertRaises(Exception, self.create_Organizer_userNull)

	def create_Organizer(self, name):
		user = User.objects.create(username='Organizer1', email='Organizer1@email.com')
		org = Organizer(name=name, user = user)
		org.save()
		sport = Sport.objects.create(name = 'sport1')
		org.sports.add(sport)
		return org

	def test_Organizer_nameShort(self):
		org = self.create_Organizer("Organizer1")
		
		self.assertTrue(isinstance(org, Organizer))
		self.assertEqual(org.__unicode__(), org.name)

	def test_Organizer_nameLong(self):
		self.assertRaises(Warning, self.create_Organizer, "this is a really long name , this is a really long name")
		
	def test_Organizer_nameNull(self):
		self.assertRaises(Exception, self.create_Organizer, None)
		
	def test_Organizer_volNotNull(self):
		org = self.create_Organizer("Organizer1")
		userVol = User.objects.create(username='Volunteer1', email='volunteer1@email.com')
		vol = Volunteer.objects.create(name = 'Volunteer1', user = userVol)
		org.volunteersSubcribed.add(vol)
		
		self.assertTrue(isinstance(org, Organizer))
		
	def create_Organizer_sportNull(self):
		user = User.objects.create(username='Organizer1', email='Organizer1@email.com')
		org = Organizer(name="Organizer1", user = user)
		org.save()
		return org
		
	def test_Organizer_sportNull(self):
		org = self.create_Organizer_sportNull()
		self.assertRaises(Exception, self.create_Organizer_sportNull)		
		
	def test_Organizer_eventNotNull(self):
		org = self.create_Organizer("Organizer1")
		sport = Sport.objects.create(name = 'sport2')
		ev = Event.objects.create(name="event1", date=datetime.date(2010, 1, 1), organizer=org)
		ev.sports.add(sport) 
		
		self.assertTrue(isinstance(org, Organizer))
		
		
