from django import forms

class UserForm(form.Form):
	username = forms.CharField(max_length=30)
	password = forms.CharField()
	

class VolunteerForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    username = forms.CharField()
    phone = forms.
