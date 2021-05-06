from urllib.request import Request, urlopen
import shutil
import datetime ,time 
from datetime import date,timedelta



weekdayNum=datetime.datetime.now().weekday()
current_time = datetime.datetime.now()
right_now=time.strftime("%H%M")
# if weekdayNum < 5:
#     if right_now == "1800":
#         print("1800")
#     else:
#         sysdate=current_time.strftime("%d%m")
#         sysday= int(current_time.strftime("%d"))
#         print(sysday)
# elif weekdayNum == 5 :
#     sysday= current_time.strftime("%d")-1



if weekdayNum<5:
    if right_now < '18:00':
        if(weekdayNum==0):
            filedate = (date.today() - timedelta(days = 3)).strftime("%d%m%y")
        else:
            filedate = (date.today() - timedelta(days = 1)).strftime("%d%m%y")


link = f"https://www.bseindia.com/download/BhavCopy/Equity/EQ{filedate}_CSV.ZIP"

header = {
    'Accept-Encoding': 'gzip, deflate, sdch, br',
    'Accept-Language': 'fr-FR,fr;q=0.8,en-US;q=0.6,en;q=0.4',
    'Host': 'www.bseindia.com',
    'Referer': 'https://www.bseindia.com/',
    'User-Agent': 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}


def download_file(link, file_name, length):
    try:
        req = Request(link, headers=header)
        with open(file_name, 'wb') as writer:
            request = urlopen(req, timeout=3)
            shutil.copyfileobj(request, writer, length)
    except Exception as e:
        print('File cannot be downloaded:', e)
    finally:
        print('File downloaded with success!')

file_name = 'EQ'+filedate+'_CSV.ZIP'
length = 2048
download_file(link, file_name, length)

