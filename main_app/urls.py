from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name="home"),
  path('user/signup/', views.signup, name='signup'),
  path('profile/<int:user_id>/', views.profile, name='profile'),
  path('profile/<int:user_id>/profile_form/', views.profile_form, name='profile_form'),
  path('elogs/', views.elogs_index, name="index"),
  path('elogs/<int:user_id>/', views.elogs_detail, name='detail'),
  path('elogs/create/', views.ElogCreate.as_view(), name='elogs_create'),
  path('elogs/<int:pk>/update/', views.ElogUpdate.as_view(), name='elogs_update'),
  path('elogs/<int:pk>/delete/', views.ElogDelete.as_view(), name='elogs_delete'),
]