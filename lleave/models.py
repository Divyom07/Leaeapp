from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# Create your models here.



    
    
class LeaveApplication(models.Model):
    fdate = models.DateField()
    tdate = models.DateField()
    type_of_leave = models.CharField(max_length=20, default='')
    reason = models.CharField(max_length = 500, default = '')
    authuser = models.ForeignKey(User,on_delete=models.CASCADE, default="", null =True, db_constraint=False)
    status = models.BooleanField('Approved', default = False)
    reject = models.BooleanField('Reject', default = False)
    pending = models.BooleanField('Pending', default = True)
    

    def __str__(self):
        return self.reason

class type_of_leave(models.Model):
    typeofLeave = models.CharField(max_length=50)
    
    def __str__(self):
        return self.typeofLeave
    
    
class gender(models.Model):
    gender = models.CharField(max_length = 50)
    
    
    def __str__(self):
        return self.gender
    
    
    
class Martial_status(models.Model):
    stat = models.CharField(max_length =50)

    
    

    