from django.urls import  path
from .views import IncomeCategoryView,IncomeAddView,IncomeView
urlpatterns = [
    path('category/',IncomeCategoryView.as_view(),name='income_category'),
    path('create/',IncomeAddView.as_view(),name='income_add'),
    path('',IncomeView.as_view(),name='income'),
]