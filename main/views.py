from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def mainn(request):
	return HttpResponse("hello world")
