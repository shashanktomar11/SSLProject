from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Post

class CustomUserCreationForm(UserCreationForm):
	
	first_name = forms.CharField(required=True)
	last_name = forms.CharField(required=True)
	email = forms.EmailField(required=True)

	class Meta:
		model = CustomUser
		fields = ('username', 'first_name', 'last_name', 'email', 'image')
	
class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'username', 'email')

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'cover']
