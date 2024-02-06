from django.db import models
from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.contrib.auth.models import AbstractUser


PAY_TERM=(
    ('Select','Select'),
    ('Daily','Daily'),
    ('Weekly','Weekly'),
    ('Half of Month','Half of Month'),
    ('Monthly','Monthly'),
    ('Half of Year','Half of Year'),
    ('Yearly','Yearly')
)
ACTION=(
    ('Select','Select'),
    ('View','View'),
    ('Edit','Edit'),
    ('Delete','Delete')
)

class Role_And_Permission(models.Model):
    #role=models.CharField(max_length=1000,null=True,blank=True)
    group=models.ForeignKey(Group,on_delete=models.CASCADE,null=True,blank=True)
    permission=models.ManyToManyField(Permission,blank=True)

    def __str__(self):
        return self.group.name
    
class Action(models.Model):
    actions=models.CharField(max_length=1000,choices=ACTION,default='Select')


class Update_Message(models.Model):
    message=models.TextField(null=True,blank=True)
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message




