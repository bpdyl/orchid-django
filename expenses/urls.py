from django.urls import  path
from .views import ExpenesCategoryView,ExpensesAddView,ExpenseView
urlpatterns = [
    path('category/',ExpenesCategoryView.as_view(),name='expenses_category'),
    path('create/',ExpensesAddView.as_view(),name='expenses_add'),
    path('',ExpenseView.as_view(),name='expenses'),
]