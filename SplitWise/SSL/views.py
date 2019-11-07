from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import *
from django.template import loader
from django.shortcuts import render
from .forms import *

'''def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")'''
'''def index(request):
    latest_question_list = Friend.objects.order_by('money_owed')[:5]
    output = ', '.join([q.user_id for q in latest_question_list])
    template = loader.get_template('SSL/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))'''

def index(request):
    user_id=''
    form = NameForm()
    formg= GroupForm()
    if request.method == 'POST':
        if 'friend' in request.POST:
            form = NameForm(request.POST)
            if form.is_valid():
                userid = form.cleaned_data['your_name']
                f = Friend(user_id=userid)
                f.save()
                form=NameForm()
                return HttpResponseRedirect("/SSL/")
        elif 'group' in request.POST:
            formg = GroupForm(request.POST)
            if formg.is_valid():
                group_name = formg.cleaned_data['group_name']
                x = formg.cleaned_data['friends']
                g = Group(name=group_name)
                g.save()
                for f in x:
                    m = Membership(friend=f, group =g)
                    m.save()
                    #print(m)
                return HttpResponseRedirect("/SSL/")    
        else:
            for g in Group.objects.all():
                if g.name in request.POST:
                    money = 0
                    m = Membership.objects.filter(group = g)
                    for x in m:
                        if x.money_owed != 0:
                            money = 1
                    if money == 0:
                        g.delete()
            return HttpResponseRedirect("/SSL/")  
                        

    else:
        form=NameForm()
    #return render(request, 'index1.html', {'form': form}) 

    groups = Group.objects.order_by('name')[:]
    #output = ', '.join([q.name for q in latest_question_list])
    money = []
    for g in groups:
        m = Membership.objects.filter(group = g)
        money.append(0)
        for x in m:
            if x.who_owes_who == "They owe you":
                money[-1] = money[-1] + int(x.money_owed)
                x.friend.money_owed = x.friend.money_owed + int(x.money_owed)
            else:
                money[-1] = money[-1] - int(x.money_owed)
                x.friend.money_owed = x.friend.money_owed - int(x.money_owed)
    money = [int(i) for i in money]           
    friends = Friend.objects.order_by('money_owed')[:]
    mylist = zip(groups,money)
    template = loader.get_template('SSL/index1.html')
    context = {
        'friends': friends,
        'groups':groups,
        'form':form,
        'formg':formg,
        'money':money,
        'mylist':mylist
    }
    return HttpResponse(template.render(context, request))

def friend(request,f):
    
    #output = ', '.join([q.name for q in latest_question_list])

    friends = Friend.objects.order_by('money_owed')[:]
    
    x = Friend.objects.filter(user_id = f)
    groups = Membership.objects.filter(friend = x[0])
    template = loader.get_template('SSL/index2.html')
    context = {
        #'friends': friends,
        'groups':groups,
        #'form':form
    }

    return HttpResponse(template.render(context, request))

def group(request,g):
    
    x = Group.objects.filter(name = g)


    friends = Membership.objects.filter(group = x[0])
    #print(friends[0].friend.user_id)
    print(friends)
    template = loader.get_template('SSL/index3.html')
    context = {
        'friends': friends,
        #'groups':groups,
        #'form':form
    }

    return HttpResponse(template.render(context, request))
    





		
   