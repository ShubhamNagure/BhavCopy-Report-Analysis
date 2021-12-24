from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
import redis ,json

# Create your views here.

r = redis.Redis(
host='127.0.0.1',
port='6379')


def rendAllStocks(request):
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