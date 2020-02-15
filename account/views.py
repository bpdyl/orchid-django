from django.shortcuts import render,redirect
from django.contrib import messages
from django.views import View
from .models import Account
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.mixins import LoginRequiredMixin
import random
# Create your views here.
from django.shortcuts import HttpResponse
import datetime
from income.models import Income
from mail.mail import sendmailtouser

class LoginView(View):
    template_name = 'login.html'

    def get(self,request):
        if request.user.is_authenticated:
            return redirect('dashboard')
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
            return redirect('login')




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
            if sendmailtouser(subject="Account is created",
                              message=f"Thank you for creating account! {f} your account is created please login to access your dashboard",
                              recipient_list=[e,]
                              ):
                messages.add_message(request,messages.SUCCESS,"Email is sent")
            else:
                messages.add_message(request,messages.ERROR,"Email can not send")

            return redirect('login')
        else:
            messages.add_message(request,messages.ERROR,"password does not match")
            return redirect('signup')


class DashboardView(LoginRequiredMixin,View):
    login_url = '/account/login'
    template_name = 'dashboard.html'
    def get(self,request):
        x = Income.objects.getIncomeByCategory(request.user.id)
        category = list(x.keys())
        amount = list(x.values())
        new_amount = []
        for a in amount:
            if a==None:
                new_amount.append(0.0)
            else:
                new_amount.append(a)
        color_list = ['#4e73df', '#1cc88a', '#36b9cc','#2e59d9', '#17a673', '#2c9faf']
        bcolor = []
        hovercolor = []
        l = len(amount)
        for i in range(0,l):
            bcolor.append(color_list[random.randint(0,5)])
            hovercolor.append(color_list[random.randint(0,5)])
        context = {
            'dayincome':Income.objects.getTotalIncomeOfToday(request.user.id),
            'category':category,
            'amount':new_amount,
            'bcolor':bcolor,
            'hcolor':hovercolor,
        }
        return render(request,self.template_name,context)