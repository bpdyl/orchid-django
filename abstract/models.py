from django.db import models
from account.models import Account

class Category(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(Account,on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100,unique=True)

    class Meta:
        abstract = True
        unique_together = ('user_id','title')


class Abs(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField(null=True,blank=True)
    slug = models.SlugField(unique=True)
    date = models.DateField(auto_now=True)
    class Meta:
        abstract=True
