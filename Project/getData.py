#!/usr/bin/python3
from urllib.request import Request, urlopen
import shutil ,os
import datetime ,time 
from datetime import date,timedelta

from zipfile import ZipFile
import pandas as pd


# flag_download_file
def get_filedate():
    weekdayNum = datetime.datetime.now().weekday()
    current_time = datetime.datetime.now()
    right_now = time.strftime("%H%M")

    if weekdayNum < 5:
        if right_now < '18:00':
            if (weekdayNum == 0):
                filedate = (date.today() - timedelta(days=3)).strftime("%d%m%y")
            else:
                filedate = (date.today() - timedelta(days=1)).strftime("%d%m%y")
        else:
            print("AFTER 6 PM ")
            filedate = date.today().strftime("%d%m%y")
            print(filedate)
    else:
        print("WEEKENDS")
        filedate = (date.today() - timedelta(days=weekdayNum - 4)).strftime("%d%m%y")

    return filedate





def download_file(link, file_name, length):

    ##downloding file from site
    header = {
        'Accept-Encoding': 'gzip, deflate, sdch, br',
        'Accept-Language': 'fr-FR,fr;q=0.8,en-US;q=0.6,en;q=0.4',
        'Host': 'www.bseindia.com',
        'Referer': 'https://www.bseindia.com/',
        'User-Agent': 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }

    try:
        req = Request(link, headers=header)
        with open(file_name, 'wb') as writer:
            request = urlopen(req, timeout=3)
            shutil.copyfileobj(request, writer, length)
            print('File downloaded with success!')
            flag_download_file=True
    except Exception as e:
        print('File cannot be downloaded:', e)
    return flag_download_file
        



"""create directory and move zip file there and unzip there."""

def move_and_unzip(file_name,filedate):

    #create folder with file date
    directory = f"{filedate}" 
    cwd=os.getcwd()
    parent_dir = f"{cwd}/util/data"
    print(parent_dir)

    path = os.path.join(parent_dir, directory)
    mode = 0o777
    os.mkdir(path,mode)

    #move file to newly created dir
    # source_dir = 'F:/BhavCopy-Report-Analysis/BhavCopy-Report-Analysis/Project/'
    #source_dir = 'C:/Users/shubh/Projekt/Project/' 
    source_dir = cwd+'/'
    target_dir = f'{cwd}/util/data/{filedate}'
    # shutil.copy(os.path.join(source_dir, file_name), target_dir)
    shutil.copy(f"{source_dir}{file_name}", target_dir)

    #change dir to unzip that file
    os.chdir(target_dir)
    with ZipFile(file_name, 'r') as zip:

        zip.printdir()
        print('Extracting all the files now...')
        zip.extractall()
        print('Done!')

    #header are removed and created input file.
    csv_file_name ='EQ'+filedate+'.CSV'
    #df=pd.read_csv(csv_file_name)
    #df.to_csv('input.csv', index_label=None, header=False)

    ldir=os.listdir()
    for f in ldir:
         if f==csv_file_name:
             flag_move_and_unzip = True
    print("File moved and unzipped",flag_move_and_unzip)
    os.chdir(cwd)
    return flag_move_and_unzip

def handle_getDate():
    ##creating dynamic filedate based on business days
    filedate = get_filedate()
    link = f"https://www.bseindia.com/download/BhavCopy/Equity/EQ{filedate}_CSV.ZIP"

    file_name = 'EQ' + filedate + '_CSV.ZIP'
    length = 2048

    #DOWNLOAD- file logic
    flag_download_file=download_file(link, file_name, length)

    ##basic operations
    flag_move_and_unzip= move_and_unzip(file_name,filedate)

    if flag_download_file & flag_move_and_unzip:
        return True
    return False



if __name__ == "__main__":
    handle_getDate()


