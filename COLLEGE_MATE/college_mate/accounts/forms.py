from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
#from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.modelfields import PhoneNumberField
from .models import UserProfile

class RegistrationForm(UserCreationForm):
	email=forms.EmailField(required=True)
	#phone=PhoneNumberField()


	class Meta:
		model=User
		fields=(
		'username',
		'first_name',
		'last_name',
		'email',
		#'phone',
		'password1',
		'password2',

		)

		def save(self,commit=True):
			user=super(RegistrationForm,self).save(commit=False)
			user.first_name=self.cleaned_data['first_name']
			user.last_name=self.cleaned_data['last_name']
			user.email=self.cleaned_data['email']
			#phone=self.cleaned_data['phone']

			if commit:
				user.save()

			return user


class EditProfileForm(UserChangeForm):

	class Meta:
		model=User
		fields=(
				'email',
				'first_name',
				'last_name',
				#'phone',
				'password',


				)

class ProfileForm(forms.ModelForm):
	desciption = forms.CharField(required=True)
	# phone = forms.
	class Meta:
		model = UserProfile
		fields = (
			'desciption',
			'phone',
			'image',
		)
