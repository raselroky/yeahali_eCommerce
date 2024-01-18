from django.db import models


class Contact_Us(models.Model):
    name=models.CharField(max_length=1000,null=True,blank=True)
    email=models.CharField(max_length=1000,null=True,blank=True)
    reason=models.CharField(max_length=1000,null=True,blank=True)
    message=models.TextField(null=True,blank=True)
    dates=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

