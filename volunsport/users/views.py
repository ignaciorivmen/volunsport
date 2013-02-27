from django.http import HttpResponse, HttpResponseRedirect
from users.models import Volunteer, Organizer, Event, VolunteerForm, OrganizerForm, EventForm, UserForm, Event_Volunteer, Event_VolunteerForm
from django.template import Context, loader
from django.shortcuts import render_to_response, get_object_or_404,    render
from django.http import Http404
from django.template import RequestContext

from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.forms.models import inlineformset_factory
from models import User 
from datetime import datetime
from django.contrib.auth import authenticate, login


#statics

def index(request):
	return render_to_response('index.html')

def about(request):
	return render_to_response('about.html')

def notices(request):
	return render_to_response('notices.html')

def resources(request):
	return render_to_response('resources.html')


def login(request):
	log = 0	
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			print 'valid'
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				print 'user'
				if user.is_active:
					print 'active'
					login(request, user)
					return HttpResponseRedirect('')
#				else:
#					log=1
#			else:
#				log=2
	else:
		form = UserForm()
	return render_to_response("login.html", RequestContext(request, {'form' : form}))
	

#{% url 'django.contrib.auth.views.login' %}

def selectregister(request):
	return render_to_response('selectregister.html')

# Volunteer views

def volunteers_index(request):
	volunteer_list = Volunteer.objects.all()
	return render_to_response('users/volunteer/index.html', {'volunteer_list': volunteer_list})

def volunteer_details(request, volunteer_id):
	#v = get_object_or_404(Volunteer, vk = volunteer_id)
	#return render_to_response('users/volunteer/details.html', {'volunteer': v}, context_instance=RequestContext(request))
	v = Volunteer.objects.get(id=volunteer_id)
	return render_to_response('users/volunteer/details.html', {'volunteer':v})

def volunteer_events_before(request,volunteer_id):
	vol= Volunteer.objects.get(id=volunteer_id)
	event_vol_list = Event_Volunteer.objects.filter(volunteer = vol)
	event_list = [] 
	for event_vol in event_vol_list:
		ev=event_vol.event
		if datetime.now().date() >= ev.date:
			event_list.append(ev)
			
	return render_to_response('users/volunteer/index_events.html', {'event_list': event_list})


def volunteer_events_after(request,volunteer_id):
	vol= Volunteer.objects.get(id=volunteer_id)
	event_vol_list = Event_Volunteer.objects.filter(volunteer = vol)
	event_list = [] 
	for event_vol in event_vol_list:
		ev=event_vol.event
		if datetime.now().date() <= ev.date:
			event_list.append(ev)
			
	return render_to_response('users/volunteer/index_events.html', {'event_list': event_list})

def volunteer_exp(request,volunteer_id):
	vol= Volunteer.objects.get(id=volunteer_id)
	event_vol_list = Event_Volunteer.objects.filter(volunteer = vol)
	exp_list = [] 
	for exp_vol in event_vol_list:
		if exp_vol.experience:
			ex=exp_vol.experience	
	return render_to_response('users/volunteer/index_exp.html', {'exp_list': exp_list})




# Organizer views

def organizers_index(request):
        organizer_list = Organizer.objects.all()
        return render_to_response('users/organizer/index.html', {'organizer_list': organizer_list})

def organizer_details(request, organizer_id):
        o = get_object_or_404(Organizer, id = organizer_id)
        return render_to_response('users/organizer/details.html', {'organizer': o})

def organizer_events(request,organizer_id):
	org= Organizer.objects.get(id=organizer_id)
	event_list = Event.objects.filter(organizer = org)
	return render_to_response('users/event/index.html', {'event_list': event_list})


def organizer_events_before(request,organizer_id):
	org= Organizer.objects.get(id=organizer_id)
	ev_list = Event.objects.filter(organizer = org)
	event_list = [] 
	for ev in ev_list:
		if datetime.now().date() >= ev.date:
			event_list.append(ev)
	return render_to_response('users/volunteer/index_events.html', {'event_list': event_list})

def organizer_events_after(request,organizer_id):
	org= Organizer.objects.get(id=organizer_id)
	ev_list = Event.objects.filter(organizer = org)
	event_list = [] 
	for ev in ev_list:
		if datetime.now().date() <= ev.date:
			event_list.append(ev)			
	return render_to_response('users/volunteer/index_events.html', {'event_list': event_list})





# Event views

def events_index(request):
        event_list = Event.objects.all()
        return render_to_response('users/event/index.html', {'event_list': event_list})

def event_details(request, event_id):
        e = get_object_or_404(Event, id = event_id)
#	event_vol_list = Event_Volunteer.objects.filter(event = e)
        return render_to_response('users/event/details.html', {'event': e},)


#Experience

def experience_index(request):
	exp_list = Event_Volunteer.objects.all()
        return render_to_response('users/event_volunteer/index.html', {'exp_list': exp_list})

def experience_details(request,exp_id):
	e = get_object_or_404(Event_Volunteer, id = exp_id)
        return render_to_response('users/event_volunteer/details.html', {'exp': e},)



#Forms

def volunteer_register(request):
	if request.method == 'POST':
		form = VolunteerForm(request.POST, request.FILES)
   		if form.is_valid():
			form.save()			
	  		return HttpResponseRedirect('/volunteers/')
	else:
		form = VolunteerForm()
	return render_to_response("users/volunteer/register.html", RequestContext(request, {'form' : form}))
	

def organizer_register(request):
	if request.method == 'POST':
		form = OrganizerForm(request.POST, request.FILES)
   		if form.is_valid():
			form.save()
	  		return HttpResponseRedirect('/organizers/')
	else:
		form = OrganizerForm()
	return render_to_response("users/organizer/register.html", RequestContext(request, {'form' : form}))

def event_register(request):
	if request.method == 'POST':
		form = EventForm(request.POST, request.FILES)
   		if form.is_valid():
			form.save()
	  		return HttpResponseRedirect('/events/')
	else:
		form = EventForm()
	return render_to_response("users/event/register.html", RequestContext(request, {'form' : form}))

def event_volunteer_register(request):
	if request.method == 'POST':
		form = Event_VolunteerForm(request.POST)
   		if form.is_valid():
			form.save()
	  		return HttpResponseRedirect('/events/')
	else:
		form = Event_VolunteerForm()
	return render_to_response("users/event_volunteer/event_volunteer_register.html", RequestContext(request, {'form' : form}))


def register(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
   		if form.is_valid():
			form.save()
	  		return HttpResponseRedirect('/volunteerreg/')
	else:
		form = UserForm()
	return render_to_response("users/register.html", RequestContext(request, {'form' : form}))



