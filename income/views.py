from django.shortcuts import render,redirect
from django.views import View
from .forms import IncomeCateogyForm,IncomeFrom
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class IncomeCategoryView(LoginRequiredMixin,View):
    template_name = 'income_category.html'
    login_url = '/account/login'

    def get(self,request):
        context = {
            'form':IncomeCateogyForm()
        }
        return render(request,self.template_name,context)

    def post(self,request,*args,**kwargs):
        form = IncomeCateogyForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user_id= request.user.id
            data.save()
            messages.add_message(request,messages.SUCCESS,"Saved Successfully")
            return redirect('dashboard')
        else:
            messages.add_message(request,messages.ERROR,"sorry error occured")
            return redirect('dashboard')



class IncomeAddView(LoginRequiredMixin,View):
    login_url = '/account/login'
    template_name = 'add_income.html'
    def get(self,request):
        context = {
            'form': IncomeFrom()
        }
        return render(request,self.template_name,context)

    def post(self,request,*args,**kwargs):
        form = IncomeFrom(request.POST,request.FILES or None)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,"Successfully added")
            return redirect('dashboard')
        else:
            messages.add_message(request,messages.ERROR,"sorry can not added")
            return redirect('dashboard')

class IncomeView(LoginRequiredMixin,View):
    template_name = 'income.html'
    login_url = '/account/login'

    def get(self,request):
        return render(request,self.template_name)