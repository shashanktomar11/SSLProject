from django.shortcuts import render, redirect, HttpResponse

# Create your views here.

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from splitwise.forms import CustomUserCreationForm#, EditProfileForm
from splitwise.forms import *

from .models import *
from django.template import loader

from django.template import RequestContext
from django.db.models import Q

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class EditProfile(generic.CreateView):
	form_class = ProfileUpdateForm
	success_url = reverse_lazy('login')
	template_name = 'editprofile.html'

#def edit_profile_view(request): 
  
#	if request.method == 'POST': 
#		form = ProfileUpdateForm(request.POST, instance=request.user) 
  
#		if form.is_valid(): 
#			form.save() 
#			return redirect('success') 
#	else:
#		form = ProfileUpdateForm() 
#		return render(request, 'editprofile.html', {'form' : form}) 
  
  
def success(request):
	me = User.objects.get(username=request.user.get_username())
	usr = request.user.get_username()
	RANGE_SHORT = 's'
	RANGE_MID = 'm'
	RANGE_LONG = 'l'
	RANGE_CHOICES = (
		(RANGE_SHORT, 'Short '),
		(RANGE_MID, 'Mid rbjkiange'),
		(RANGE_LONG, 'Long range')
	)

	friend_form = FriendForm()
	
	xyz=Friend.objects.filter(person1=me)
	#print(xyz)
	final_choices=()
	for e in xyz:
		#print(str(e.person2))
		thistuple = (str(e.person2), str(e.person2))
		#print(thistuple)
		final_choices = final_choices + (thistuple,)
	#print(final_choices)
	group_form = GroupForm(final_choices)
	#group_form.fields['friends'].choices=RANGE_CHOICES
	if request.method == 'POST':
		if 'friend' in request.POST:
			friend_form = FriendForm(request.POST)
			if friend_form.is_valid():
				friend_id = friend_form.cleaned_data['your_name']
				if User.objects.filter(username=friend_id).exists():
					friend = User.objects.get(username=friend_id)
					if friend == me:
						print('F')
					elif Friend.objects.filter(person1=me,person2=friend).exists() or Friend.objects.filter(person1=friend,person2=me).exists():
						print("f")
					else:
						f = Friend(person1=me,person2=friend)
						f1 = Friend(person1=friend,person2=me)

						print('hi')
						f.save()
						f1.save()
				return HttpResponseRedirect("/splitwise/success/")

						print(f)
		if 'group' in request.POST:
			
			group_form = GroupForm(final_choices, request.POST)
			if group_form.is_valid():
				name = group_form.cleaned_data['group_name']
				people = group_form.cleaned_data['friends']
				g = Group(group_name=name)
				g.save()
				for p in people:
					member = User.objects.get(username=p)
					m = Membership(friend = member, group = g)
					m.save()
					#print(member)
				return HttpResponseRedirect("/splitwise/success/") 
	else:
		friend_form=FriendForm()
		group_form=GroupForm(final_choices)
		#group_form.fields['friends'].choices=[]
	
	friends = Friend.objects.values_list('person1')
	
	context = {
		'friend_form' : friend_form,
		'group_form' : group_form,
		'friends' : friends
	}
	

	template = loader.get_template('home.html') 
	#return render(request, 'home.html',
         #  context_instance=RequestContext(request))
	return HttpResponse(template.render(context, request))

#def x(request):
#	print("f")
#	return HttpResponse('')
