from django.shortcuts import render,redirect
from django.views import View
from .forms import IncomeCateogyForm,IncomeFrom
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import IncomeCategory,Income
from django.views.generic import UpdateView
from django.urls import reverse_lazy
# Create your views here.
class IncomeCategoryView(LoginRequiredMixin,View):
    template_name = 'income_category.html'
    login_url = '/account/login'

    def get(self,request):
        context = {
            'form':IncomeCateogyForm(),
            'category':IncomeCategory.objects.filter(user_id=request.user.id)
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
            'form': IncomeFrom(request.user.id)
        }
        return render(request,self.template_name,context)

    def post(self,request,*args,**kwargs):
        form = IncomeFrom(request.user.id,request.POST,request.FILES or None)
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
        context = {
            'income':Income.objects.filter(category__in=IncomeCategory.objects.filter(user_id=request.user.id))
        }
        return render(request,self.template_name,context)


class EditView(UpdateView):
    template_name = 'edit_income.html'
    form = IncomeFrom
    fields = ['title', 'description', 'price', 'image', 'category']
    success_url = reverse_lazy('income')

    def get_context_data(self, **kwargs):
        context = super(EditView, self).get_context_data()
        context['form'] = IncomeFrom(self.request.user.id, instance=Income.objects.get(slug=self.kwargs['slug']))
        return context

    def get_object(self, queryset=None):
        queryset = Income.objects.filter(slug=self.kwargs['slug'])
        return super(EditView, self).get_object(queryset)
