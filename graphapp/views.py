from django.shortcuts import render, redirect
from gwpy.timeseries import TimeSeries
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

import matplotlib.pyplot as plt
import numpy as np 
import math
from pylab import *

# Create your views here.
from .models import *
from .forms import CreateUserForm


def index_view(request):


	return render(request, 'index.html')


def files_view(request):
	return render(request, 'files.html')

def about_view(request):
	return render(request, 'about.html')




def test(request):
	ch="K1:CAL-CS_PROC_DARM_STRAIN_DBL_DQ"
	start=1361343353
	end=start+10
	data = TimeSeries.get(ch, start, end, host="133.100.214.16", port=31200) 
	context = {'start':start, 'ch':ch, 'data':data}
	return render(request, 'test.html', context)

def return_graph():
	cache_file = "home/detchar/cache/Cache"
	data = TimeSeries.read()

def graph(request):
	context['graph'] = return_graph()
	return render(request, 'graph.html', context)

def create_csv():
	# create csv file
	# iterater for data
	i = 0

	data = TimeSeries.read('templates/K-K1_C-1342415264-32.gwf')
	# gwf file data has different "dialect", so it must be defined
	csv.register_dialect('gwfDialect', delimiter=" ", quoting=csv.QUOTE_NONE)
	with open(file, 'w') as csvfile:
		# each line will have gps,data
		writer = csv.writer(csvfile)
			
		while i < (end - start):
			writer.writerow({data[i],start_gps+i})
			i = i + 1
	return file


def registerPage(request):
	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request, 'Account created for ' + user)
			return redirect('login')
	context = {'form':form}
	return render(request, 'register.html', context)

def loginPage(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('/')

		else:
			messages.info(request, 'Username OR password is incorrect')
			return

	context = {}
	return render(request, 'login.html', context)

