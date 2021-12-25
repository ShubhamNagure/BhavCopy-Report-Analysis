from django.shortcuts import render
from rest_framework import routers, serializers, viewsets

from MainApp.models import BhavcopyRec
from .serializers import BhavcopyRecSerializer

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

import redis ,json

from django.http import JsonResponse

# Create your views here.

r = redis.Redis(
host='127.0.0.1',
port='6379')


def getAllStocks(request):
    print("All data load on startup")

    if request.method =='GET':
    
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

        
        return JsonResponse(jsonObj, safe=False)
    
    
def searchStocks(request):
    pass

