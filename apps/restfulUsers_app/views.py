# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from time import gmtime, strftime
from models import *

# Create your views here.
def index(request):
	return render(request, 'restfulUsers_app/index.html', { "users": User.objects.all() })

def newPage(request):
	return render(request, 'restfulUsers_app/newPage.html')

def editPage(request, id):
	return render(request, 'restfulUsers_app/editPage.html', { "user": User.objects.get(id = id) })

def userPage(request, id):
	return render(request, 'restfulUsers_app/userPage.html', { "user": User.objects.get(id = id) })

def createUser(request):
	User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
	return redirect('/users/' + str(User.objects.last().id))

def updateUser(request, id):
	x = User.objects.get(id=id)
	x.first_name = request.POST['first_name']
	x.last_name = request.POST['last_name']
	x.email = request.POST['email']
	x.save()
	return redirect('/users/' + str(User.objects.get(id=id).id))

def destroy(request, id):
	User.objects.get(id=id).delete()
	return redirect('/users/')