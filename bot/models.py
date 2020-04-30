from django.db import models
from django.contrib.auth import get_user_model
import hashlib
import os

User = get_user_model()
'''class Knowledge(models.Model):
    title = models.CharField(max_length=30,null=False,blank=False)
    description = models.TextField(blank=False,null=False)
    score = models.IntegerField(default=0,blank=False,null=False)
    modify_user = models.ForeignKey(User, on_delete=models.CASCADE)
#    knowledge_code = models.CharField(max_length=32,default=md5_func,blank=False,null=False,unique=True)
    add_time = models.DateTimeField(auto_now_add=True)

class KnowledgeStatus(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    like_or_unlike = models.CharField(max_length=10,blank=True,null=True,default="so_so")
    knowledge = models.ForeignKey(Knowledge,on_delete=models.CASCADE)

class Policy(models.Model):
    title = models.CharField(max_length=30,null=False,blank=False)
    description = models.TextField(blank=False,null=False)
    url = models.CharField(max_length=300,blank=True,null=True)
    score = models.IntegerField(default=0,blank=False,null=False)
    modify_user = models.ForeignKey(User, on_delete=models.CASCADE)
    policy_code = models.CharField(max_length=32,default=md5_func,blank=False,null=False,unique=True)
    add_time = models.DateTimeField(auto_now_add=True)

class PolicyStatus(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    like_or_unlike = models.CharField(max_length=10,blank=True,null=True,default="so_so")
    policy = models.ForeignKey(Policy,on_delete=models.CASCADE)
'''
class TelegramChat(models.Model):
    chat_id = models.CharField(max_length=50,null=False,blank=False,unique=True)
#    knowledge_pack = models.ManyToManyField(KnowledgeStatus,null=True,blank=True)
#    policy_pack = models.ManyToManyField(PolicyStatus,null=True,blank=True)
