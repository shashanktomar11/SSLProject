from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Profile
#from .models import CustomUser
#from .models import Post1

class CustomUserCreationForm(UserCreationForm):
	
	#first_name = forms.CharField(required=True)
	#last_name = forms.CharField(required=True)
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email')

	def save(self, commit=True):
		user=super(CustomUserCreationForm, self).save(commit=False)
		#user.first_name = first_name
		#user.last_name = last_name
		#user.email = email

		if commit:
			user.save()

		return user

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['bio', 'image']

	def save(self, commit=True):
		user=super(ProfileUpdateForm, self).save(commit=False)
		#user.first_name = first_name
		#user.last_name = last_name
		#user.email = email

		if commit:
			user.save()

		return user

#class EditProfileForm(forms.Form):
	
#	first_name = forms.CharField(required=True)
#	last_name = forms.CharField(required=True)
#	email = forms.EmailField(required=True)
#	image = forms.ImageField(required=True)

#	class Meta:
#		model = User
#		fields = ('first_name', 'last_name', 'email', 'image')

#	def save(self, commit=True):
#		user=super(EditProfileForm, self).save(commit=False)
		#user.first_name = first_name
		#user.last_name = last_name
		#user.email = email

#		if commit:
#			user.save()

#		return user
