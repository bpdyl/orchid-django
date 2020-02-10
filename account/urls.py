from django.urls import path
from .views import LoginView,SignupView,DashboardView
urlpatterns = [
  path('login/',LoginView.as_view(),name='login'),
  path('signup/',SignupView.as_view(),name='signup'),
  path('dashboard/',DashboardView.as_view(),name='dashboard'),
]