from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser): # To regiser a new user

    email=models.EmailField(max_length=255,unique=True)

    def __str__(self) -> str:
        return self.username


class UserInfo(models.Model):
    Name= models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    Mobile=models.CharField( max_length=150,null=True)
    Email= models.CharField( max_length=150,null=True)
    Country=models.CharField( max_length=150,null=True)
    City=models.CharField( max_length=150,null=True)
    Date_of_Birth=models.DateField()
    Contract_Start_Date=models.DateField()
    Contract_End_Date=models.DateField()
    active=models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.Email