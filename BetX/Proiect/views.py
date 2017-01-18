from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
	return HttpResponse("This is the home Page")

def detail(request, pronostic_id):
	return HttpResponse("Te uiti la pronosticul:%s" % pronostic_id)

def results(request, pronostic_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(response % pronostic_id)

def vote(request, pronostic_id):
	return HttpResponse("Votezi pronosticul:%s" % pronostic_id)