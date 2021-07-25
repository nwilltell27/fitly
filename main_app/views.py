from django.shortcuts import render, redirect
from .models import Elog, UserProfile
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class ElogCreate(CreateView):
  model = Elog
  fields = '__all__'

class ElogUpdate(UpdateView):
  model = Elog
  fields = ['name', 'distance_miles', 'length_of_time', 'reps_laps', 'weight_pounds', 'intensity', 'pace_minutes_per_mile', 'calories_burned']

class ElogDelete(DeleteView):
  model = Elog
  success_url = 'elogs/detail.html'

def home(request):
  return render(request, 'home.html')

def elogs_index(request):
  elogs = Elog.objects.all()
  return render(request, 'elogs/index.html', {'elogs': elogs})
'''
def elogs_index(request):
  elogs = UserProfile.objects.()
  return render(request, 'elogs/index.html', {'elogs': elogs})
'''
def elogs_detail(request, user_id):
  userprofile = UserProfile.objects.get(id=user_id)
  return render(request, 'elogs/detail.html', {'userprofile': userprofile})
  