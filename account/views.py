from django.shortcuts import render,redirect
from django.contrib import messages
from django.views import View
from .models import Account
from django.contrib.auth import authenticate,login,logout
# Create your views here.

class LoginView(View):
    template_name = 'login.html'

    def get(self,request):
        return render(request,self.template_name)

    def post(self,request,*args,**kwargs):
        e = request.POST.get('email')
        p = request.POST.get('pass')
        user = authenticate(email=e,password=p)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.add_message(request,messages.ERROR,"Login Credential does not match")
            return redirect('loging')




class SignupView(View):
    template_name = 'signup.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self,request,*arg,**kwargs):
        f = request.POST.get('fname')
        l = request.POST.get('lname')
        e = request.POST.get('email')
        p1 = request.POST.get('pass1')
        p2 = request.POST.get('pass2')
        if p1==p2:
            Account.objects.create_user(e,firstname=f,lastname=l,password=p1)
            messages.add_message(request,messages.SUCCESS,"Signup successfull")
            return redirect('login')
        else:
            messages.add_message(request,messages.ERROR,"password does not match")
            return redirect('signup')


class DashboardView(View):
    template_name = 'dashboard.html'

    def get(self,request):
        return render(request,self.template_name)