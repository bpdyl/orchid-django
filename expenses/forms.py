from .models import Expenses,ExpensesCategory
from django import forms
from account.models import Account
from .models import ExpensesCategory
class ExpensesCategoryForm(forms.ModelForm):
    #title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Category'}))

    class Meta:
        model = ExpensesCategory
        fields ='__all__'


class ExpensesForm(forms.ModelForm):
    # category =  forms.ModelChoiceField(widget=forms.Select(attrs={'class':'form-control'}),queryset=None)
    #
    # def __init__(self,id,*args,**kwargs):
    #     super(ExpensesForm, self).__init__(*args,**kwargs)
    #     self.fields['category'].queryset=ExpensesCategory.objects.filter(user_id=1)
    class Meta:
        model = Expenses
        fields ='__all__'