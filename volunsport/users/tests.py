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
		vol.subcribedToEvent.add(eventvol)
		
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
		
class EventTest(TestCase):

	def create_Event(self, name):
		sport = Sport.objects.create(name = 'sport1')
		dat = datetime.date.today()
		user = User.objects.create(username='Organizer1', email='Organizer1@email.com')
		org = Organizer(name="organizer1", user = user)
		org.save()
		org.sports.add(sport)
		ev = Event(name=name, organizer = org, date = dat)
		ev.save()
		ev.sports.add(sport)
		return ev

	def test_Event_nameShort(self):
		ev = self.create_Event("Event1")
		
		self.assertTrue(isinstance(ev, Event))
		self.assertEqual(ev.__unicode__(), ev.name)

	def test_Event_nameLong(self):
		self.assertRaises(Warning, self.create_Event, "this is a really long name , this is a really long name")
		
	def test_Event_nameNull(self):
		self.assertRaises(Exception, self.create_Event, None)
		
	def create_Event_dateNull(self):
		name = "Event1"
		return Event.objects.create(name=name)
		
	def test_Event_dateNull(self):
		self.assertRaises(Exception, self.create_Event_dateNull)
		
	def test_Event_volNotNull(self):
		ev = self.create_Event("Event1")
		ev.save()
		userVol = User.objects.create(username='Volunteer1', email='volunteer1@email.com')
		vol = EventVolunteer.objects.create(state = "AWAITING" , event = ev)
		ev.volunteers.add(vol)
		
		self.assertTrue(isinstance(ev, Event))
		
	def create_Event_sportNull(self):
		user = User.objects.create(username='Organizer1', email='Organizer1@email.com')
		sport = Sport.objects.create(name = 'sport1')
		org = Organizer(name="organizer1", user = user)
		org.sports.add(sport)
		org.save()
		ev = Event(name="Event1", organizer = org)
		ev.save()
		return ev
		
	def test_Event_sportNull(self):
		self.assertRaises(Exception, self.create_Event_sportNull)		
		
	def create_Event_organizerNull(self, name):
		sport = Sport.objects.create(name = 'sport1')
		ev = Event(name=name)
		ev.sports.add(sport)
		ev.save()
		return ev	
		
	def test_Event_organizerNull(self):
		self.assertRaises(Exception, self.create_Event_organizerNull)

class SportTest(TestCase):
	
	def create_Sport(self, name):
		spo = Sport.objects.create(name = name)
		return spo

	def test_Sport_nameShort(self):
		spo = self.create_Sport("Sport1")
		
		self.assertTrue(isinstance(spo, Sport))
		self.assertEqual(spo.__unicode__(), spo.name)

	def test_Sport_nameLong(self):
		self.assertRaises(Warning, self.create_Sport, "this is a really long name , this is a really long name")
		
	def test_Sport_nameNull(self):
		self.assertRaises(Exception, self.create_Sport, None)
				
	def test_Sport_eventNotNull(self):
		
		spo = self.create_Sport("sport1")
		dat = datetime.date.today()
		user = User.objects.create(username='Organizer1', email='Organizer1@email.com')
		org = Organizer(name="organizer1", user = user)
		org.save()
		org.sports.add(spo)
		ev = Event(name="Event1", organizer = org, date = dat)
		ev.save()
		ev.sports.add(spo)
		spo.events.add(ev)
		
		self.assertTrue(isinstance(spo, Sport))
				
	def test_Sport_volNotNull(self):
		spo = self.create_Sport("sport1")
		user = User.objects.create(username='Volunteer1', email='Volunteer1@email.com')
		vol = Volunteer(name = "volunteer1", user = user)
		vol.save()
		spo.volunteers.add(vol)
		
		self.assertTrue(isinstance(spo, Sport))
				
	def test_Sport_organizerNotNull(self):
		spo = self.create_Sport("Sport1")
		user = User.objects.create(username='Organizer1', email='Organizer1@email.com')
		org = Organizer(name="organizer1", user = user)
		org.save()
		org.sports.add(spo)
		spo.organizers.add(org)		

		self.assertTrue(isinstance(spo, Sport))

class EventVolunteerTest(TestCase):
	
	def create_EventVolunteer(self, experience):
		sport = Sport.objects.create(name = 'sport1')
		dat = datetime.date.today()
		user = User.objects.create(username='Organizer1', email='Organizer1@email.com')
		org = Organizer(name="organizer1", user = user)
		org.save()
		org.sports.add(sport)
		ev = Event(name="Event1", organizer = org, date = dat)
		ev.save()
		ev.sports.add(sport)
		evVol = EventVolunteer(state = "AWAKENING", event=ev , experience=experience)
		evVol.save()
		return evVol

	def test_EventVolunteer_experienceShort(self):
		evVol = self.create_EventVolunteer("Experience 1")
		
		self.assertTrue(isinstance(evVol, EventVolunteer))
		self.assertEqual(evVol.__unicode__(), evVol.state)

	def test_EventVolunteer_experienceLong(self):
		self.assertRaises(Warning, self.create_EventVolunteer, "this is a really long experience , this is a really long experience , this is a really long experience , this is a really long experiencethis is a really long experience , this is a really long experiencethis is a really long experience , this is a really long experiencethis is a really long experience , this is a really long experience , this is a really long experience , this is a really long experience , this is a really long experience , this is a really long experience")
		
	def test_EventVolunteer_experienceNull(self):
		evVol = self.create_EventVolunteer(None)
		
		self.assertTrue(isinstance(evVol, EventVolunteer))
		
	def create_EventVolunteer_stateNull(self):
		return EventVolunteer.objects.create(valuation=5, experience="great")
		
	def test_EventVolunteer_stateNull(self):
		self.assertRaises(Exception, self.create_EventVolunteer_stateNull)

	def test_EventVolunteer_volNotNull(self):
		evVol = self.create_EventVolunteer("EventVolunteer1")
		userVol = User.objects.create(username='Volunteer1', email='volunteer1@email.com')
		vol = Volunteer(name="volunter1", user=userVol)
		vol.save()
		evVol.volunteers.add(vol)
		
		self.assertTrue(isinstance(evVol, EventVolunteer))
		
	def create_EventVolunteer_EventNull(self):
		evVol = EventVolunteer(state = "AWAKENING")
		evVol.save()
		return evVol
		
	def test_EventVolunteer_EventNull(self):
		self.assertRaises(Exception, self.create_EventVolunteer_EventNull)		


