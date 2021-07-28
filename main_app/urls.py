from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('user/signup/', views.signup, name='signup'),
  path('user/index', views.user_index, name='user_index'),
  path('elogs/', views.elogs_index, name="index"),
  path('elogs/<int:user_id>/', views.elogs_detail, name='detail'),
  path('elogs/<int:pk>/create/', views.ElogCreate.as_view(), name='elogs_create'),
  path('elogs/<int:pk>/update/', views.ElogUpdate.as_view(), name='elogs_update'),
  path('elogs/<int:pk>/delete/', views.ElogDelete.as_view(), name='elogs_delete'),
  path('account/signup/', views.signup, name='signup'),
] 