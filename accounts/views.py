from django.shortcuts import render
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import UpdateView
from django.contrib.auth.models import User
from .forms import IzmeniProfil
# Create your views here.

class ProfileUpdate(UserPassesTestMixin,UpdateView):
	model=User
	form_class=IzmeniProfil
	template_name='registration/profile_form.html'
	def test_func(self):
		userobj=User.objects.get(pk=self.kwargs['pk'])
		return userobj == self.request.user
