from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('dashboard/<int:user_id>/', views.user_dashboard, name='dashboard'), 
]