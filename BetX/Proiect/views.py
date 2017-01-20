from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic.edit import DeleteView, UpdateView
from django.views.generic.list import ListView

from . import models
from . import forms

from .forms import SignUpForm
from .models import Pronostic
# Create your views here.

def pronosticuri(request):
    latest_pronostic_list = Pronostic.objects.order_by('-publication_date')
    context = {'latest_pronostic_list': latest_pronostic_list}
    return render(request, 'Proiect/pronostic.html', context)

def detail(request, pronostic_id):
	return HttpResponse("Te uiti la pronosticul:%s" % pronostic_id)

def results(request, pronostic_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(response % pronostic_id)

def vote(request, pronostic_id):
	return HttpResponse("Votezi pronosticul:%s" % pronostic_id)

def home(request):

	form = SignUpForm(request.POST or None)

	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.save()

	return render(request,
				  'Proiect/signup.html',
				  locals(),
		 		  )

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
                return redirect('pronosticuri')
            else:
                context['error_message'] = 'Wrong username or password!'
    context['form'] = form
    return render(request, 'Proiect/login.html', context)


def logout_view(request):
    if request.method == 'GET':
        logout(request)
        return redirect('login')


def user_profile(request, pk):
    if request.method == 'GET':
        user_profile = models.UserProfile.objects.get(pk=pk)
    context = {
        'user_profile': user_profile,
    }
    return render(request, 'Proiect/user_profile.html', context)


def edit_user_profile(request, pk):
    user_profile = models.UserProfile.objects.get(pk=pk)
    form = forms.ProfileForm(initial={
        'first_name': user_profile.first_name,
        'last_name': user_profile.last_name
    })
    if request.method == 'POST':
        form = forms.ProfileForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            user_profile.first_name = first_name
            user_profile.last_name = last_name
            user_profile.save()
            return redirect('user_profile', pk=pk)

    context = {
        'user_profile': user_profile,
        'form': form,
    }
    return render(request, 'Proiect/edit_profile.html', context)
