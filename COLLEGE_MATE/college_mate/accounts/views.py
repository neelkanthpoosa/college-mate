# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from accounts.forms import (
	RegistrationForm,
	EditProfileForm,
	)
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from .forms import EditProfileForm,ProfileForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
# Create your views here.
#@login_required

def register(request):
	if request.method=='POST':
		form=RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/account')
	else:
		form=RegistrationForm()

		args={'form': form}
		return render(request,'accounts/reg_form.html',{'form':form})

@login_required
def profile(request):
	args={'user':request.user}
	return render(request,'accounts/profile.html')

@login_required
def edit_profile(request):
	if request.method=='POST':
		form=EditProfileForm(request.POST,instance=request.user)
		form1 = ProfileForm(request.POST,instance=request.user.userprofile)
		if form.is_valid() and form1.is_valid():
			form.save()
			form1.save()
			return redirect('/account/profile')

	else:
		form=EditProfileForm(instance=request.user)
		form1=ProfileForm(instance=request.user.userprofile)

	return render(request,'accounts/update_profile.html',{'form':form,'form1':form1})


@login_required
def change_password(request):
	if request.method=='POST':
		form=PasswordChangeForm(data=request.POST,user=request.user)

		if form.is_valid():
			form.save()
			update_session_auth_hash(request,form.user)
			return redirect('/account/profile/')

		else:
			return redirect('/account/change-password')


	else:
		form=PasswordChangeForm(user=request.user)

		args={'form':form}
		return render(request,'accounts/change_password.html', args)
