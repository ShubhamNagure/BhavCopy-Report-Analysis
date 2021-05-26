from django.shortcuts import render

from .models import *
from django.core.cache import cache

import redis ,json

r = redis.Redis(
host='192.168.99.100',
port='6379')


def redisDBandCache(request):
    filter_rec = request.GET.get('stock')
    if filter_rec is not None:
        if cache.get(filter_rec):
            uperc=filter_rec.upper()
            jsonObj = cache.get(uperc)
            # print(newlist)
            print("DATA COMING FROM CACHE")
        else:
            uperc=filter_rec.upper()
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
    else:
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

    context = {'jsonObj': jsonObj}
    return render(request, 'index.html', context )
