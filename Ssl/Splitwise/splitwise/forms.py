from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import *
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

class FriendForm(forms.Form):
	your_name = forms.CharField(label="Friend's username", max_length=100)

class GroupForm(forms.Form):
    group_name = forms.CharField(label='Group name', max_length=100)
    RANGE_SHORT = 's'
    RANGE_MID = 'm'
    RANGE_LONG = 'l'
    RANGE_CHOICES = (
        (RANGE_SHORT, 'Sho'),
        (RANGE_MID, 'Mid range'),
        (RANGE_LONG, 'Long range')
    )
    friends = forms.MultipleChoiceField(choices=[])

    def __init__(self, user, *args, **kwargs):
        super(GroupForm, self).__init__(*args, **kwargs)
        self.fields['friends'] = forms.MultipleChoiceField(
            choices=user
        )

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


