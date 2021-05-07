from urllib.request import Request, urlopen
import shutil ,os
import datetime ,time 
from datetime import date,timedelta

from zipfile import ZipFile
import pandas as pd



weekdayNum=datetime.datetime.now().weekday()
current_time = datetime.datetime.now()
right_now=time.strftime("%H%M")


if weekdayNum<5:
    if right_now < '18:00':
        if(weekdayNum==0):
            filedate = (date.today() - timedelta(days = 3)).strftime("%d%m%y")
        else:
            filedate = (date.today() - timedelta(days = 1)).strftime("%d%m%y")
    else:
        print("AFTER 6 PM ")
        filedate = date.today().strftime("%d%m%y")
        print(filedate)
else:
    print("WEEKENDS")
    filedate = (date.today() - timedelta(days = weekdayNum-4)).strftime("%d%m%y")



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
            print('File downloaded with success!')
    except Exception as e:
        print('File cannot be downloaded:', e)

        
file_name = 'EQ'+filedate+'_CSV.ZIP'
length = 2048
download_file(link, file_name, length)


"""create directory and move zip file there and unzip there."""

def move_and_unzip(file_name):
    #create folder with file date
    directory = f"{filedate}"
    parent_dir = "F:/BhavCopy-Report-Analysis/BhavCopy-Report-Analysis/Project/util/data/"

    path = os.path.join(parent_dir, directory)
    os.mkdir(path)

    #move file to newly created dir
    source_dir = 'F:/BhavCopy-Report-Analysis/BhavCopy-Report-Analysis/Project/util/'
    target_dir = f'F:/BhavCopy-Report-Analysis/BhavCopy-Report-Analysis/Project/util/data/{filedate}'
    shutil.move(os.path.join(source_dir, file_name), target_dir)

    #change dir to unzip that file
    os.chdir(target_dir)
    with ZipFile(file_name, 'r') as zip:

        zip.printdir()
        print('Extracting all the files now...')
        zip.extractall()
        print('Done!')

    #header are removed and created input file.
    csv_file_name ='EQ'+filedate+'.csv'
    df=pd.read_csv(csv_file_name)
    df.to_csv('input.csv', index_label=None, header=False)

move_and_unzip(file_name)





