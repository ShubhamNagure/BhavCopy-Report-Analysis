import redis,json
r = redis.Redis(
host='127.0.0.1',
port='6379')
search_val = 'ABB LTD.'
req_str = f'bhavcopy:{search_val}*'
mylist= []
sn = 0 
for key in r.scan_iter(req_str):
    mylist.append(key.decode('utf-8'))
    
#print(mylist)

mylistdeteils =[]
for l in mylist:
    mylistdeteils.append(r.hgetall(l))

finallist=[]
for x in mylistdeteils:
    finallist={k.decode('utf-8').strip(): v.decode('utf-8').strip() for k ,v in x.items()}
#     print(finallist)

jsonObj=json.dumps(finallist)
                
print("**********",jsonObj)

myallkeys= []
for k in r.keys():
    myallkeys.append(k.decode('utf-8'))

#print(myallkeys)
myallvalues =[]
badkey = []
counter = 0
for s in myallkeys:
    if counter <1555:
        myallvalues.append(r.hgetall(s))
        counter +=1
    elif( counter > 1550 & counter < 1560):
        badkey.append(s)

#print(myallvalues)

print(badkey)

#finalAllList =[]
#for n in myallvalues:
#    finalAllList.append({k.decode('utf-8').strip(): v.decode('utf-8').strip() for k ,v in n.items()})

#newlist = sorted(finalAllList, key=lambda k: k['SC_CODE']) 
#print(newlist)
