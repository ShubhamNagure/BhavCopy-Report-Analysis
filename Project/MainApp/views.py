from django.shortcuts import render,redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import *
from django.core.cache import cache


import redis ,json

r = redis.Redis(
host='127.0.0.1',
port='6379')

def rendAllStocks():
    print("All data load on startup")
    myallkeys = []
    for k in r.keys():
        myallkeys.append(k)

    myallvalues =[]
    for s in myallkeys:
        myallvalues.append(r.hgetall(s))

    finalAllList =[]
    for n in myallvalues:
        finalAllList.append({k.decode('utf-8').strip(): v.decode('utf-8').strip() for k ,v in n.items()})
    newlist = sorted(finalAllList, key=lambda k: k['SC_CODE']) 
    jsonObj= json.dumps(newlist,separators=(',', ':')).replace("'", r"\'")
    return jsonObj
    
def searchStocks(request):
    filter_rec = request.GET.get('stock')
 
    uperc=filter_rec.upper()
    if cache.get(uperc):
        # uperc=filter_rec.upper()
        jsonObj = cache.get(uperc)
        # print(newlist)
        print("DATA COMING FROM CACHE")
    else:
        # uperc=filter_rec.upper()
        req_str = f'bhavcopy:{uperc}*'
        mylist= []
        for key in r.scan_iter(req_str):
            mylist.append(key.decode('utf-8'))
        mylistdeteils = []
        for l in mylist:
            mylistdeteils.append(r.hgetall(l))
        finallist=[]
        for x in mylistdeteils:
            finallist.append({k.decode('utf-8').strip(): v.decode('utf-8').strip() for k ,v in x.items()})

        newlist = sorted(finallist, key=lambda k: k['SC_CODE']) 
        jsonObj= json.dumps(newlist,separators=(',', ':')).replace("'", r"\'")
        cache.set(uperc, jsonObj,timeout=500)
        print("DATA COMING FROM DB")
    return jsonObj

@login_required(login_url='login')
def redisDBandCache(request):
    filter_rec = request.GET.get('stock')

    if filter_rec is not None:
        jsonObj=searchStocks(request)
    else:
        jsonObj=rendAllStocks()
    context = {'jsonObj': jsonObj}
    return render(request, 'index_new.html', context )


def registerPage(request):
    if request.user.is_authenticated:
	    return render(request,'login.html')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return render(request, 'login.html')
        context = {'form':form}
        return render(request, 'register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        filter_rec = request.GET.get('stock')

        if filter_rec is not None:
            jsonObj=searchStocks(request)
        else:
            jsonObj=rendAllStocks()
        context = {'jsonObj': jsonObj}
        return render(request, 'index_new.html', context )
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                jsonObj=rendAllStocks()
                context = {'jsonObj': jsonObj}
                return render(request,'index_new.html',context)
            else:
                messages.info(request, 'Username OR password is incorrect')
        context = {}
        return render(request, 'login.html', context)


def logoutUser(request):
	logout(request)
	return redirect('login')