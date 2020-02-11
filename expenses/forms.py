from .models import Expenses,ExpensesCategory
from django import forms
from account.models import Account
from .models import ExpensesCategory
class ExpensesCategoryForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Category'}))

    class Meta:
        model = ExpensesCategory
        fields =['title',]


class ExpensesForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    price = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    category = forms.ModelChoiceField(queryset=ExpensesCategory.objects.all(),
                                      widget=forms.Select(attrs={'class': 'form-control'}))
    # def __init__(self,id,*args,**kwargs):
    #     super(ExpensesForm, self).__init__(*args,**kwargs)
    #     self.fields['category'].queryset=ExpensesCategory.objects.filter(user_id=1)
    class Meta:
        model = Expenses
        fields ='__all__'