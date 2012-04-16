# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import logout

def main_page(request):
	return render_to_response(
		'main_page.html',
		{'user': request.user}
	)

def user_page(request, username):
	user = get_object_or_404(User, username=username)
	bookmarks = user.bookmark_set.all()
	return render_to_response(
		'user_page.html',
		{'username': username, 'bookmarks': bookmarks}
	)

def logout_page(request):
	logout(request)
	return HttpResponseRedirect('/')