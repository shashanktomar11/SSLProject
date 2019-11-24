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

						
		if 'group' in request.POST:
			
			group_form = GroupForm(final_choices, request.POST)
			if group_form.is_valid():
				name = group_form.cleaned_data['group_name']
				people = group_form.cleaned_data['friends']
				g = Group(group_name=name)
				g.save()
				m = Membership(friend = me, group =g)
				m.save()
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
	
	friends = Friend.objects.filter(person1=me)
	groups = Membership.objects.filter(friend=me)
	print(groups)

	edit_profile_form = ProfileUpdateForm()
	if request.method == 'POST':
		if 'edit_profile' in request.POST:
			print(request.user.profile.bio)
			edit_profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
			if edit_profile_form.is_valid():
				#edit_profile_form.save()
				#bio = edit_profile_form.cleaned_data['bio']
				#print(bio)
				#image = edit_profile_form.cleaned_data['image']
				#print(request.FILES['image'])
				#z = Profile.objects.get(user = me)
				#z.bio = bio
				#z.image = "profile_image/"+str(request.FILES['image'])
				#print(Profile.objects.get(user = me).image)
				#z.save()
				edit_profile_form.save()
				#print(bio)
	else:
		edit_profile_form=ProfileUpdateForm()
	
	context = {
		'friend_form' : friend_form,
		'group_form' : group_form,
		'friends' : friends,
		'groups' : groups,
		'edit_profile_form' : edit_profile_form
	}
	

	template = loader.get_template('home.html') 
	#return render(request, 'home.html',
         #  context_instance=RequestContext(request))
	return HttpResponse(template.render(context, request))

def friend(request,f):
	me = request.user
	x = Friend.objects.filter(person1__username=me)

	z=0
	a=''
	for y in x:
		if(y.person2.username==f):
			z = y.money_owed
			a = str(y.person2)

	template = loader.get_template('expanded_friend.html')
	context = {
		'z' : z,
		'a' : a
	}
	return HttpResponse(template.render(context, request))

def group(request,g):
	me=request.user
	template = loader.get_template('expanded_group.html')
	x = ''
	context = {
		'x' : x
	}
	return HttpResponse(template.render(context, request))

def transaction(request):
	me = request.user
	xyz=Friend.objects.filter(person1=me)
	#print(xyz)
	final_choices=()
	for e in xyz:
		#print(str(e.person2))
		thistuple = (str(e.person2), str(e.person2))
		#print(thistuple)
		final_choices = final_choices + (thistuple,)
	involved_form = InvolvedForm(final_choices)
	if request.method=='POST':
		if 'involved' in request.POST:
			involved_form=InvolvedForm(final_choices, request.POST)
			if involved_form.is_valid():
				people = involved_form.cleaned_data['friends']
				for p in people:
					print(p)
				request.session['people'] = people
				request.session['choices'] = final_choices
				return HttpResponseRedirect('/splitwise/transaction/form/')
	else:
		involved_form=InvolvedForm(final_choices)
	template = loader.get_template('transaction.html')
	x=''
	context = {
		'involved_form':involved_form
	}
	return HttpResponse(template.render(context, request))

def transaction_form(request):
	me = request.user
	people = request.session.get('people')
	final_choices = ()
	final_choices = final_choices + ((me.username,me.username),)
	for p in people:
		thistuple = (str(p),str(p))
		final_choices = final_choices + (thistuple,)
	choices = request.session.get('choices')
	template = loader.get_template('transaction_form.html')
	transaction_form = TransactionForm(final_choices)
	if request.method == 'POST':
		if 'transaction' in request.POST:
			transaction_form=TransactionForm(final_choices, request.POST)
			if transaction_form.is_valid():
				desc = transaction_form.cleaned_data['description']
				who_paid = transaction_form.cleaned_data['who_paid']
				print(who_paid)
				amt = transaction_form.cleaned_data['amount']
				split = transaction_form.cleaned_data['split']
				print(split)
				tag = transaction_form.cleaned_data['tag']
				shares = []
				for i in final_choices:
					data = transaction_form.cleaned_data[i[0]+' (%)']
					mytuple = (str(i[0]),data)
					shares.append(mytuple)
				payer = User.objects.get(username=who_paid[0])
				print(payer)
				if split == 'equal':
					for p in final_choices:
						print(p[0])
						user = User.objects.get(username=p[0])

				else:
					for p in final_choices:
						print(p[0])

				return HttpResponseRedirect('/splitwise/transaction/form/')
	else:
		transaction_form = TransactionForm(final_choices)

	context ={
		'transaction_form' : transaction_form
	}
	return HttpResponse(template.render(context,request))