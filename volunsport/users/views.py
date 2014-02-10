from django.http import HttpResponse
from users.models import Volunteer, Organizer, Event
from django.template import Context, loader
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404

# Volunteer views

def volunteersIndex(request):
	volunteer_list = Volunteer.objects.all()
	return render_to_response('templates/users/volunteer/index.html', {'volunteer_list': volunteer_list})

def volunteerDetails(request, volunteer_id):
	v = Volunteer.objects.get(id=volunteer_id)
	return render_to_response('templates/users/volunteer/details.html', {'volunteer':v})

# Organizer views

def organizersIndex(request):
        organizer_list = Organizer.objects.all()
        return render_to_response('users/organizer/index.html', {'organizer_list': organizer_list})

def organizerDetails(request, organizer_id):
        o = get_object_or_404(Organizer, ok = organizer_id)
        return render_to_response('users/organizer/details.html', {'organizer': o})

# Event views

def eventsIndex(request):
        event_list = Event.objects.all()
        return render_to_response('users/event/index.html', {'event_list': event_list})

def eventDetails(request, event_id):
        e = get_object_or_404(Event, ek = event_id)
        return render_to_response('users/event/details.html', {'event': e})

# Sport views

def sportsIndex(request):
        sport_list = Sport.objects.all()
        return render_to_response('users/sport/index.html', {'sport_list': sport_list})

def sportDetails(request, sport_id):
        e = get_object_or_404(Sport, ek = sport_id)
        return render_to_response('users/sport/details.html', {'sport': e})

# EventVolunteer views

def eventVolunteerIndex(request):
        eventVolunteer_list = EventVolunteer.objects.all()
        return render_to_response('users/eventVolunteer/index.html', {'eventVolunteer_list': eventVolunteer_list})

def eventVolunteerDetails(request, eventVolunteer_id):
        e = get_object_or_404(EventVolunteer, ek = eventVolunteer_id)
        return render_to_response('users/eventVolunteer/details.html', {'eventVolunteer': e})
