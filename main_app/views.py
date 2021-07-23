from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import ProfileForm

# Create your views here.
def home(request):
  return render(request, 'home.html')

def signup(request):
  return render(request, 'user/signup.html')

def profile(request):
  profile_form = ProfileForm()
  return render(request, 'user/profile.html', {'profile_form': profile_form})