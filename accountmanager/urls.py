"""accountmanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import (
PasswordResetView,
PasswordResetConfirmView,
PasswordResetDoneView,
PasswordResetCompleteView
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include('account.urls')),
    path('income/',include('income.urls')),
    path('expenses/',include('expenses.urls')),
    path('forget-password/',PasswordResetView.as_view(
        template_name='password_rest_form.html'
    ),name='forget-password'),
    path('reset-password/confirmation/<str:uidb64>/<str:token>',
         PasswordResetConfirmView.as_view(
             template_name='change_password.html'
         ),
         name='password_reset_confirm'),
    path('rest-password/done',PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('rest-password/complete',PasswordResetCompleteView.as_view(
        template_name='password_complete.html'
    ),
         name='password_reset_complete')
]
