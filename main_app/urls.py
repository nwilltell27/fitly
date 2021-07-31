from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('user/signup/', views.signup, name='signup'),
  path('user/<int:user_id>/', views.user_index, name='user_index'),
  path('user/create/', views.ProfileCreate.as_view(), name='profile_create'),
  # Exercise Log CRUD
  path('elogs/', views.elogs_index, name="index"),
  path('elogs/<int:user_id>/', views.elogs_detail, name='detail'),
  path('elogs/create/', views.ElogCreate.as_view(), name='elogs_create'),
  path('elogs/<int:pk>/update/', views.ElogUpdate.as_view(), name='elogs_update'),
  path('elogs/<int:pk>/delete/', views.ElogDelete.as_view(), name='elogs_delete'),
  # Food Log CRUD
  path('flogs/', views.flogs_index, name="index"),
  path('flogs/<int:user_id>/', views.flogs_detail, name='detail'),
  path('flogs/create/', views.FlogCreate.as_view(), name='flogs_create'),
  path('flogs/<int:pk>/update/', views.FlogUpdate.as_view(), name='flogs_update'),
  path('flogs/<int:pk>/delete/', views.FlogDelete.as_view(), name='flogs_delete'),

  path('account/signup/', views.signup, name='signup'),
  path('registration/profile/', views.profile, name='profile'),
] 
