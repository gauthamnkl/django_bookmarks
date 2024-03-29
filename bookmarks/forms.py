import re
from django.contrib.auth.models import User
from django import forms

class RegistrationForm(forms.Form):
	username = forms.CharField(
		label=u'Username', 
		max_length=30
	)
	email = forms.CharField(label=u'Email')
	password1 = forms.CharField(
		label=u'Password',
		widget=forms.PasswordInput()
	)
	password2 = forms.CharField(
		label=u'Confirm Password',
		widget=forms.PasswordInput()
	)

def clean_password2(self):
	if 'password1' in self.cleaned_data:
		password1 = self.cleaned_data['password']
		password2 = self.cleaned_data['password2']
		if password1 == password2:
			return password2
	raise forms.ValidationError('Passwords do not match.')

def clean_username(self):
	username = self.cleaned_data['username']
	if not re.search(r'^\w+$', username):
		raise forms.ValidationError('Username can only contain alphanumeric characters and underscore.')
	try:
		User.objects.get(username=username)
	except UserDoesNotExist:
		return username
	raise forms.ValidationError('Username is already taken.')

class BookmarkSaveForm(forms.Form):
	url = forms.URLField(
		label = u'URL',
		widget = forms.TextInput(attrs={'size': 64})
	)

	title = forms.URLField(
		label = u'Title',
		widget = forms.TextInput(attrs={'size': 64})
	)

	tags = forms.URLField(
		label = u'Tags',
		required = False,
		widget = forms.TextInput(attrs={'size': 64})
	)