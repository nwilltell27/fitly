from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('user/signup/', views.signup, name='signup'),
  path('profile/<int:user_id>/', views.profile, name='profile'),
  path('profile/<int:user_id>/profile_form/', views.profile_form, name='profile_form'),
] 