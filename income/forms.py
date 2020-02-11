from .models import Income,IncomeCategory
from django import forms
class IncomeCateogyForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = IncomeCategory
        fields =['title',]


class IncomeFrom(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    price = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    category = forms.ModelChoiceField(queryset=IncomeCategory.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))

    class Meta:
        model = Income
        fields ='__all__'