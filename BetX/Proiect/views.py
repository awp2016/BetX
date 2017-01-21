from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.models import User

from . import models
from . import forms

from .forms import SignUpForm
from .models import Pronostic
# Create your views here.




class MatchListView(ListView):
	model = models.Match
	template_name = 'Proiect/Home.html'
	context_object_name = 'matches'




class PronosticuriListView(ListView):
	model = models.Pronostic
	template_name = 'Proiect/pronosticuri.html'
	context_object_name = "pronosticuri"
	def get_queryset(self):
		return Pronostic.objects.filter(match__pk= self.kwargs['pk']).order_by('-publication_date')

	def get_context_data(self, **kwargs):
		context = super(PronosticuriListView, self).get_context_data(**kwargs)
		context['match'] = models.Match.objects.get(pk = self.kwargs['pk'])
		return context



def results(request, pronostic_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(response % pronostic_id)

def vote(request, pronostic_id):
	return HttpResponse("Votezi pronosticul:%s" % pronostic_id)

def signup(request):
	if request.method == 'POST':
		form = forms.RegistrationForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(username=form.cleaned_data['username'],
											password=form.cleaned_data['password'])
			user_profile = models.UserProfile.objects.create(first_name = form.cleaned_data['first_name'],
															last_name = form.cleaned_data['last_name'],
															email = form.cleaned_data['email'],
															birthday = form.cleaned_data['birthday'],
															sex = form.cleaned_data['sex'],
															)
			return redirect('Login/')
	form = forms.RegistrationForm()
	context = {
		'form': form
	}
	return render(request, 'Proiect/signup.html', context)


def login_view(request):
	context = {}
	if request.method == 'GET':
		form = forms.LoginForm()
	elif request.method == 'POST':
		form = forms.LoginForm(request.POST)
		if form.is_valid():
			user = authenticate(username=form.cleaned_data['username'],
								password=form.cleaned_data['password'])
			if user:
				login(request=request,
					  user=user)
				return redirect('Home')
			else:
				context['error_message'] = 'Wrong username or password!'
	context['form'] = form
	return render(request, 'Proiect/login.html', context)


def logout_view(request):
	if request.method == 'GET':
		logout(request)
		return redirect('login')


# def user_profile(request, pk):
#     if request.method == 'GET':
#         user_profile = models.UserProfile.objects.get(pk=pk)
#     context = {
#         'user_profile': user_profile,
#     }
#     return render(request, 'Proiect/user_profile.html', context)

class UserProfileView(DetailView):

	model = models.UserProfile
	context_object_name = 'user_profile'
	template_name = 'Proiect/user_profile.html'

	def get_context_data(self, **kwargs):
		context = super(UserProfileView, self).get_context_data(**kwargs)
		context['pronostics'] = self.get_object().user.pronostics.all()
		return context

# def edit_user_profile(request, pk):
#     user_profile = models.UserProfile.objects.get(pk=pk)
#     form = forms.ProfileForm(initial={
#         'first_name': user_profile.first_name,
#         'last_name': user_profile.last_name
#     })
#     if request.method == 'POST':
#         form = forms.ProfileForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             user_profile.first_name = first_name
#             user_profile.last_name = last_name
#             user_profile.save()
#             return redirect('user_profile', pk=pk)
#
#     context = {
#         'user_profile': user_profile,
#         'form': form,
#     }
#     return render(request, 'Proiect/edit_profile.html', context)


class UserProfileUpdate(LoginRequiredMixin, UpdateView):
	model = models.UserProfile
	fields = ['first_name','last_name','birthday','sex']
	template_name = 'Proiect/edit_profile.html'
	def get_success_url(self):
		return reverse('user_profile', kwargs = {'pk':self.get_object().pk})


class AddProno(LoginRequiredMixin, CreateView):
	model = models.Pronostic
	fields = ['match','pronostic_text']
	template_name = 'Proiect/addprono.html'
	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(AddProno, self).form_valid(form)
	def get_success_url(self):
		return reverse('Home')
