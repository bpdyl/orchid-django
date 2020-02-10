from django.shortcuts import render
from django.views import View
from .forms import ExpensesCategoryForm,ExpensesForm
# Create your views here.
class ExpenesCategoryView(View):
    template_name = 'expenses_category.html'

    def get(self,request):
        context = {
            'form':ExpensesCategoryForm()
        }
        return render(request,self.template_name,context)


class ExpensesAddView(View):
    template_name = 'add_expenses.html'
    def get(self,request):
        context = {
            'form': ExpensesForm()
        }
        return render(request,self.template_name,context)

class ExpenseView(View):
    template_name = 'expenses.html'

    def get(self,request):
        return render(request,self.template_name)