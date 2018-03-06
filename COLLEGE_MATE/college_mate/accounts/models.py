# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from phonenumber_field.modelfields import PhoneNumberField

#from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class UserProfile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	desciption=models.CharField(max_length=100,default='')
	#name=models.Charfield(max_length=20,default='')
	#phone_number=PhoneNumberField()
	phone=PhoneNumberField(blank=True)
	image=models.ImageField(upload_to='profile_image',blank=True)

	def __str__(self):
		return self.user.username

def create_profile(sender,**kwargs):
	if kwargs['created']:
		user_profile=UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile,sender=User)