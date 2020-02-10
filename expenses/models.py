from django.db import models
from abstract.models import Category,Abs
# Create your models here.

class ExpensesCategoryManager(models.Manager):
    pass

class ExpensesCategory(Category):

    objects = ExpensesCategoryManager()
    class Meta:
        db_table = 'expensescategory'

class ExpensesManager(models.Manager):
    pass

class Expenses(Abs):
    image = models.ImageField(upload_to='expenses/',null=True,blank=True)
    category = models.ForeignKey(ExpensesCategory,on_delete=models.CASCADE)
    objects = ExpensesManager()

    class Meta:
        db_table = 'expenses'
