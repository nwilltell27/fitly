from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import UserProfile, User, Elog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('profile')
    else: error_message = 'Invalid Signup Data - Please Try Again'

  form = UserCreationForm()
  return render(request, 'registration/signup.html', {'form': form, 'error_message': error_message})

def profile(request):
  return render(request, 'registration/profile.html')

@login_required
def user_index(request):
  users = User.objects.all()
  return render(request, 'user/index.html', {'users': users})

class ElogCreate(LoginRequiredMixin, CreateView):
  model = Elog
  fields = [ 
    'date_time',
    'name', 
    'distance_miles', 
    'length_of_time', 
    'reps_laps', 
    'weight_pounds', 
    'intensity', 
    'pace_minutes_per_mile', 
    'calories_burned']

def get_initial(self):
    return { 'user_id': self.request.user }

class ElogUpdate(LoginRequiredMixin, UpdateView):
  model = Elog
  fields = [ 
    'name', 
    'distance_miles', 
    'length_of_time', 
    'reps_laps', 
    'weight_pounds', 
    'intensity', 
    'pace_minutes_per_mile', 
    'calories_burned']

class ElogDelete(LoginRequiredMixin,DeleteView):
  model = Elog
  success_url = '/elogs/'

@login_required
def elogs_index(request):
  elogs = Elog.objects.all()
  return render(request, 'elogs/index.html', {'elogs': elogs})

@login_required
def elogs_detail(request, user_id):
  userprofile = UserProfile.objects.get(id=user_id)
  return render(request, 'elogs/detail.html', {'userprofile': userprofile})
