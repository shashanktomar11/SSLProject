from django.shortcuts import render, redirect, HttpResponse

# Create your views here.

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from splitwise.forms import CustomUserCreationForm#, EditProfileForm
from splitwise.forms import ProfileUpdateForm


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

#class EditProfile(generic.CreateView):
#	form_class = ProfileUpdateForm
#	success_url = reverse_lazy('login')
#	template_name = 'editprofile.html'

def edit_profile_view(request): 
  
	if request.method == 'POST': 
		form = ProfileUpdateForm(request.POST, instance=request.user) 
  
		if form.is_valid(): 
			form.save() 
			return redirect('success') 
	else:
		form = ProfileUpdateForm() 
		return render(request, 'editprofile.html', {'form' : form}) 
  
  
def success(request): 
    return HttpResponse('successfuly uploaded') 
