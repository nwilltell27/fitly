from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import UserProfile, Elog

class User:
  def __init__(self, user_id, first_name, last_name, email, password):
    self.user_id = user_id
    self.first_name = first_name
    self.last_name = last_name
    self.email = email
    self.password = password

users = [
  User('juliav', 'Julia', 'Vavrinyuk', 'juliav@fitly.com', 'fitly'),
]

# Create your views here.
def home(request):
  return render(request, 'home.html')

def signup(request):
  return render(request, 'user/signup.html')

def user_index(request):
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