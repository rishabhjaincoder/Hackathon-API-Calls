from django.shortcuts import render
from django.http import HttpResponse
from main.models import *
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def mainn(request):
	return HttpResponse("hello world")

@csrf_exempt
def welcome(request):
	if (request.method=='GET'):
		# u = UserModel()
		# u.firstname = request.POST.get("firstname")
		# u.lastname = request.POST.get("lastname")
		# u.email = request.POST.get("email")
		# u.save()
		return HttpResponse("403 - Access Forbidden")
	else:
		# return HttpResponse(request)
		jsonData = json.load(request)
		u = UserModel()
		u.firstname = jsonData['firstname']
		u.lastname = jsonData['lastname']
		u.email = jsonData['email']
		u.save()
		# print(result)
		# if result != none:
		# 	return HttpResponse(result.id)
		# else:
		# 	return HttpResponse(-1)
