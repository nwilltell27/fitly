from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import UserProfile, User, Elog

# Create your views here.
def home(request):
  return render(request, 'home.html')

def signup(request):
  return render(request, 'user/signup.html')

def user_index(request):
  users = User.objects.all()
  return render(request, 'user/index.html', {'users': users})

class ElogCreate(CreateView):
  model = Elog
  fields = '__all__'

class ElogUpdate(UpdateView):
  model = Elog
  fields = ['name', 'distance_miles', 'length_of_time', 'reps_laps', 'weight_pounds', 'intensity', 'pace_minutes_per_mile', 'calories_burned']

class ElogDelete(DeleteView):
  model = Elog
  success_url = 'elogs/detail.html'

def elogs_index(request):
  elogs = Elog.objects.all()
  return render(request, 'elogs/index.html', {'elogs': elogs})

def elogs_detail(request, user_id):
  userprofile = UserProfile.objects.get(id=user_id)
  return render(request, 'elogs/detail.html', {'userprofile': userprofile})