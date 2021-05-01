from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.utils import timezone
from multiselectfield import MultiSelectField
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,username,email,password=None):
        if not email:
            raise ValueError("Please enter mandatory field email")
        user = self.model(username=username,email=self.normalize_email(email))
        user.set_password(password)
        user.save(self._db)
        return user
    def create_superuser(self,username,email,password=None):
        if not email:
            raise ValueError("Please enter mandatory field email")
        user = self.model(username=username,email=self.normalize_email(email))
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser,PermissionsMixin):
    choices = (
        ('Salamtak','Salamtak'),('Risk','Risk'),('Finance','Finance'),('AML','AML'),('OPS','OPS')
    )
    email = models.EmailField(unique=True,null=False)
    username = models.CharField(unique=True,max_length=30,null=False)
    first_name = models.CharField(max_length=30,null=True,blank=True)
    last_name = models.CharField(max_length=30,null=True,blank=True)
    access_date = models.DateTimeField(auto_now=timezone.now())
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    team = models.CharField(max_length=50,choices=choices,default="Risk")
    user_permission = MultiSelectField(choices=choices)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']