from django.db import models
from django.contrib.auth.models import User
import hashlib
import os

def create_key():
    return hashlib.md5(os.urandom(32)).hexdigest()

class AeroboxData(models.Model):
    pm   = models.FloatField(blank=True)
    temp = models.FloatField(blank=True)
    rh   = models.IntegerField(blank=True)
    co2  = models.IntegerField(blank=True)
    lon  = models.FloatField(blank=True)
    lat  = models.FloatField(blank=True)
    time = models.DateTimeField(auto_now_add=True)
#pen = models.IntegerField(blank=True) 
    #def __str__(self):
    #    return self.pm, self.temp, self.rh, self.co2, self.lon, self.lat, self.time

class Aerobox(models.Model):
    aerobox_id  = models.CharField(max_length=100,default=1)
    sitename    = models.CharField(max_length=100,default=1)
    aeroboxdata = models.ManyToManyField(AeroboxData)

class ProjectData(models.Model):
    pj_name     = models.CharField(max_length=100,default=1)
    start_time  = models.DateTimeField(auto_now_add=True)
    end_time    = models.DateTimeField(auto_now=True)
    aerobox     = models.ManyToManyField(Aerobox)

class UserExtension(models.Model):
    user         = models.ForeignKey(User,on_delete=models.CASCADE)##ForeignKey==onetoone
    u_name       = models.CharField(max_length=100,default=1)
    personal_key = models.CharField(max_length=33,blank=True,default=create_key,unique=True)
    projectdata  = models.ManyToManyField(ProjectData)

