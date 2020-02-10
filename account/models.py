from django.db import models
from django.contrib.auth.models import (
AbstractBaseUser,
BaseUserManager
)
# Create your models here.
class AccountManager(BaseUserManager):

    def create_user(self,email,firstname=None,lastname=None,contact_no=None,password=None):
        if not email:
            raise ValueError("User must have an email address")
        user = self.model(
            email=self.normalize_email(email),
            contact_no= contact_no,
            firstname=firstname,
            lastname=lastname
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,firstname=None,lastname=None,contact_no=None,password=None):
        user = self.create_user(email,firstname,lastname,contact_no,password)
        user.is_admin=True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="Enter your email",
                              unique=True)
    contact_no = models.CharField(max_length=100,null=True,blank=True,verbose_name="Contact Number",unique=True)
    firstname = models.CharField(verbose_name="First Name",max_length=100,null=True,blank=True)
    lastname = models.CharField(verbose_name="Last Name",max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects  = AccountManager()
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return True

    def has_module_perms(self,app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
