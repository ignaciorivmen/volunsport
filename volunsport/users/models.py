from django.db import models
from django.contrib.auth.models import User

from django.forms import ModelForm
from django import forms

# Generic choices

SPORTS = (
	('BA', 'BASKETBALL'),
	('BAS', 'BASEBALL'),
	('BOX', 'BOXING'),
	('CAN', 'CANOEING'),
	('CHE', 'CHESS'),
	('CRI', 'CRICKET'),
	('CYC', 'CYCLING'),
	('EQU', 'EQUESTRIAN'),
	('FEN', 'FENCING'),
	('FIS', 'FISHING'),
	('FOO', 'FOOTBALL'),
	('FUT', 'FUTSAL'),
	('GOL', 'GOLF'),
	('GYM', 'GYMNASTICS'),
	('HAN', 'HANDBALL'),
	('HOC', 'HOCKEY'),
	('HOR', 'HORSE RACING'),
	('JUD', 'JUDO'),
	('KAR', 'KARATE'),
	('KAY', 'KAYAKING'),
	('LAC', 'LACROSSE'),
	('MAR', 'MARTIAL ARTS'),
	('MOT', 'MOTOR SPORTS'),
	('PAD', 'PADDLE'),
	('ROW', 'ROWING'),
	('RUG', 'RUGBY'),
	('SAI', 'SAILING'),
	('SHO', 'SHOOTING'),
	('SKI', 'SKIING'),
	('SNO', 'SNOOKER'),
	('SUR', 'SURFING'),
	('SWI', 'SWIMMING'),
	('TAB', 'TABLE TENNIS'),
	('TAE', 'TAEKWONDO'),
	('TEN', 'TENNIS'),
	('TRI', 'TRIATHLON'),
	('VOL', 'VOLEYBALL'),
	('WAT', 'WATERPOLO'),
)

# Data models

class Volunteer(User):
	GENRE = (
		('MA', 'MALE'),
		('FE', 'FEMALE'),
	)
	WORKING_SITUATION = (
		('ST', 'Studying'),
		('WO', 'Working'),
		('UN', 'Unemployed'),
		('RE', 'Retired'),
	)
	INFORMATIC_LEVEL = (
		('EX', 'Expert'),
		('ME', 'Medium'),
		('SM', 'Small'),
	)
	SIZE = (
		('XS', 'XS'),
		('S', 'S'),
		('M', 'M'),
		('L', 'L'),
		('XL', 'XL'),
		('X2', 'XXL'),
	)
	LANGUAGES = (
		('EN', 'English'),
		('SP', 'Spanish'),
		('FR', 'French'),
                ('CH', 'Chinese'), 
                ('JP', 'Japanese'), 
                ('RU', 'Russian'), 
                ('GE', 'German'), 
                ('AR', 'Arabic'), 
                ('IT', 'Italian'), 
                ('OT', 'Other'), 
	)
	DRIVE_LICENSES = (
		('A1', 'A1'),
                ('A2', 'A2'), 
                ('A', 'A'), 
                ('B', 'B'),
                ('C1', 'C1'),
                ('C', 'C'),
                ('D1', 'D'),  
                ('BE', 'BE'), 
                ('C1E', 'C1E'), 
                ('CE', 'CE'), 
                ('D1E', 'D1E'),
                ('DE', 'DE'),  
                ('BTP', 'BTP'), 
	)

	photo = models.ImageField(upload_to='images/volunteer') 
	nationality = models.CharField(max_length=50)
	genre = models.CharField(max_length=2, choices=GENRE)
	birth_date = models.DateField()
	age = models.PositiveIntegerField()
	disability = models.NullBooleanField()
	disability_degree = models.PositiveIntegerField(null=True, blank=True)
	guardian = models.CharField(null=True, max_length=100, blank=True)	

	address = models.CharField(max_length=50)
	number = models.PositiveIntegerField(null=True, blank=True)
	floor = models.PositiveIntegerField(null=True, blank=True)
	letter = models.CharField(max_length=3,null=True, blank=True)
	city = models.CharField(max_length=25)
	state = models.CharField(max_length=25, null=True, blank=True)
	country = models.CharField(max_length=25)
	phone_number = models.CharField(max_length=15, null=True, blank=True)

	working_situation = models.CharField(max_length=2, choices=WORKING_SITUATION, blank=True)
	languages = models.CharField(max_length=3, choices=LANGUAGES)
	informatic_level = models.CharField(max_length=2, choices=INFORMATIC_LEVEL, blank=True)
	drive_licences = models.CharField(max_length=3, choices=DRIVE_LICENSES, blank=True)
	sports = models.CharField(max_length=3, choices=SPORTS)
	previous_experience = models.CharField(max_length=200, null=True, blank=True)
	
	trousers_size = models.CharField(max_length=2, choices=SIZE, null=True, blank=True)
	t_shirt_size = models.CharField(max_length=2, choices=SIZE, null=True, blank=True)
	short_size = models.CharField(max_length=2, choices=SIZE, null=True, blank=True)
	coat_size = models.CharField(max_length=2, choices=SIZE, null=True, blank=True)
	
	def __unicode__(self):
		return self.first_name

class Organizer(User):

	photo = models.ImageField(upload_to='images/organizer')
	address = models.CharField(max_length=50)
	city = models.CharField(max_length=25, null=True, blank=True)
	state = models.CharField(max_length=25, null=True, blank=True)
	country = models.CharField(max_length=25)
	cif_nif = models.CharField(max_length=25)
	razon_social = models.CharField(max_length=150)
	phone_number = models.CharField(max_length=15, null=True, blank=True)

	contact_person = models.CharField(max_length=150)
	person_phone_number = models.CharField(max_length=15)
	contact_email = models.EmailField(max_length=75)	

	website =  models.URLField(null=True, blank=True)
	facebook = models.URLField(null=True, blank=True)
	twitter = models.URLField(null=True, blank=True)

        sports = models.CharField(choices=SPORTS, max_length=3)

	def __unicode__(self):
		return self.first_name

class Event(models.Model):
	
	name = models.CharField(max_length=50)
	photo = models.ImageField(upload_to='images/event')
	address = models.CharField(max_length=50)
	city = models.CharField(max_length=25)
	state = models.CharField(max_length=25)
	country = models.CharField(max_length=25)
	date = models.DateField()
        sports = models.CharField(choices=SPORTS, max_length=30)

	description = models.CharField(max_length=300)
	
	volunteers_need = models.PositiveIntegerField()
	vacancies = models.CharField(max_length=150, null=True, blank=True)
	open_event_registration = models.DateField()
	close_event_registration = models.DateField()
	requirements = models.CharField(max_length=150)
	further_information = models.CharField(max_length=300, null=True, blank=True)
	opportunities = models.CharField(max_length = 150)

	organizer = models.ForeignKey(Organizer)
	volunteers = models.ManyToManyField(Volunteer, null=True, blank=True, through= 'Event_Volunteer')

	def __unicode__(self):
		return self.name

class Event_Volunteer(models.Model):
	volunteer = models.ForeignKey(Volunteer)
	event = models.ForeignKey(Event)
	experience = models.TextField(blank=True, null = True)


class VolunteerForm(ModelForm):
	class Meta:
		model = Volunteer
		exclude = ('is_staff','is_active','is_superuser','last_login','date_joined','groups','user_permissions',)

class OrganizerForm(ModelForm):
	class Meta:
		model = Organizer
		exclude = ('is_staff','is_active','is_superuser','last_login','date_joined','groups','user_permissions','last_name')

class EventForm(ModelForm):
	class Meta:
		model = Event
		exclude = ('volunteers',)

class Event_VolunteerForm(ModelForm):
	class Meta:
		model = Event_Volunteer
#		exclude = ('volunteers',)

class UserForm(ModelForm):
	class Meta:
		model = User
		fields = ('username', 'password')


