from django.urls import  path
from .views import IncomeCategoryView,IncomeAddView,IncomeView,EditView
urlpatterns = [
    path('category/',IncomeCategoryView.as_view(),name='income_category'),
    path('create/',IncomeAddView.as_view(),name='income_add'),
    path('update/<slug:slug>',EditView.as_view(),name="edit_income"),
    path('',IncomeView.as_view(),name='income'),
]