from django.urls import  path
from .views import (IncomeCategoryView,
                    IncomeAddView,
                    IncomeView,
                    EditView,
                    IncomeDeleteView,
                    IncomeCategoryEditView,
                    IncomeCategoryDeleteView,
                    editIncome,
                    deleteIncome,
                    deleteIncomeCategory
                    )
urlpatterns = [
    path('category/',IncomeCategoryView.as_view(),name='income_category'),
    path('create/',IncomeAddView.as_view(),name='income_add'),
    path('category-update/<slug:slug>',IncomeCategoryEditView.as_view(),name='income_category_update'),
    #path('update/<slug:slug>',EditView.as_view(),name="edit_income"),
    path('update/<slug:slug>',editIncome,name="edit_income"),
    #path('delete/<slug:slug>',IncomeDeleteView.as_view(),name="delete_income"),
    path('delete/<slug:slug>',deleteIncome,name="delete_income"),
    #path('category-delete/<slug:slug>',IncomeCategoryDeleteView.as_view(),name="delete_income_category"),
    path('category-delete/<slug:slug>',deleteIncomeCategory,name="delete_income_category"),
    path('',IncomeView.as_view(),name='income'),
]