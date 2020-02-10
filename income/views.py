from django.shortcuts import render
from django.views import View
from .forms import IncomeCateogyForm,IncomeFrom
# Create your views here.
class IncomeCategoryView(View):
    template_name = 'income_category.html'

    def get(self,request):
        context = {
            'form':IncomeCateogyForm()
        }
        return render(request,self.template_name,context)


class IncomeAddView(View):
    template_name = 'add_income.html'
    def get(self,request):
        context = {
            'form': IncomeFrom()
        }
        return render(request,self.template_name,context)

class IncomeView(View):
    template_name = 'income.html'

    def get(self,request):
        return render(request,self.template_name)