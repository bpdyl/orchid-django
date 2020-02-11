from django.db import models
from account.models import Account
from autoslug import AutoSlugField

class Category(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(Account,on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from='title')

    class Meta:
        abstract = True
        unique_together = ('user_id','title')


class Abs(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField(null=True,blank=True)
    slug = AutoSlugField(populate_from='title')
    date = models.DateField(auto_now=True)
    class Meta:
        abstract=True
