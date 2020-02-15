from django.db import models
from abstract.models import Category,Abs
from django.db.models import Sum
import datetime
from datetime import timedelta
# Create your models here.
class IncomeCategoryManager(models.Manager):
    def getAllCategory(self,user_id):
        return self.filter(user_id=user_id)


class IncomeCategory(Category):
    objects = IncomeCategoryManager()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'incomecategory'
        unique_together = ('user_id','title')


class IncomeManager(models.Manager):
    def getTotalIncomeOfMonth(self,user_id):
        return self.filter(date__month=datetime.date.today().month,
                           date__year=datetime.date.today().year,
                           category__in=IncomeCategory.objects.filter(user_id=user_id)).aggregate(Sum('price'))

    def getTotalIncomeOfToday(self,user_id):
        return self.filter(date=datetime.date.today(),
                           category__in=IncomeCategory.objects.filter(user_id=user_id)).aggregate(Sum('price'))

    def getYesterdayIncome(self,user_id):
        yesterday = datetime.date.today()-timedelta(days=1)
        return self.filter(date=yesterday,
                           category__in=IncomeCategory.objects.filter(user_id=user_id)).aggregate(Sum('price'))
    def getIncomeofLastMonth(self,user_id):
        today = datetime.date.today()
        year = today.year
        month = today.month
        previousmonth = month-1
        if previousmonth==0:
            previousmonth=12
            year=year-1
        return self.filter(date__month=previousmonth,
                           date__year=year,
                           category__in=IncomeCategory.objects.filter(user_id=user_id)).aggregate(Sum('price'))

    def getIncomeByCategory(self,user_id):
        all_category = IncomeCategory.objects.getAllCategory(user_id)
        bycategory = {}
        for x in all_category:
            s = self.filter(category=x).aggregate(Sum('price'))
            bycategory[x.title]=s['price__sum']
        return bycategory

class Income(Abs):
    image = models.ImageField(upload_to='income/', null=True, blank=True)
    category = models.ForeignKey(IncomeCategory, on_delete=models.CASCADE)
    objects = IncomeManager()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'income'