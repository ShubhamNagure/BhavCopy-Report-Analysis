from django.shortcuts import render
from rest_framework import routers, serializers, viewsets

from MainApp.models import BhavcopyRec
from .serializers import BhavcopyRecSerializer
from django.core.cache import cache

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

import redis ,json

from django.http import JsonResponse

# Create your views here.

r = redis.Redis(
host='127.0.0.1',
port='6379')


def pullDataFromRedis():
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
    return newlist

def getAllStocks(request):
    if request.method =='GET':
        redis_list=pullDataFromRedis()
        serialize= BhavcopyRecSerializer(data=redis_list,many=True)
        return JsonResponse(serialize.initial_data,safe=False)
    
    
def searchStocks(request,name):
    filter_rec = name
 
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
        serialize= BhavcopyRecSerializer(data=newlist,many=True)
        return JsonResponse(serialize.initial_data,safe=False)

