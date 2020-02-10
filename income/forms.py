from .models import Income,IncomeCategory
from django import forms
class IncomeCateogyForm(forms.ModelForm):
    class Meta:
        model = IncomeCategory
        fields ='__all__'


class IncomeFrom(forms.ModelForm):
    class Meta:
        model = Income
        fields ='__all__'