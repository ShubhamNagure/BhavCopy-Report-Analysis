import getData
import loader
import os

import schedule
import time


def job():

    """ `STEP-1` : get data from site """
    flag=getData.handle_getDate()

    """ `STEP-2` : delete old and load new data """
    print(flag)
    if flag:
        flag_loader= loader.handle_loader()
    else:
        print("LOADER FAILED : cannot load data")

    if flag and flag_loader:
        print("SUCCESS: Data EXTRACTED and LOADED Successfully !!!")
    elif not flag:
        print("FAILURE :DOWNLOAD AND EXTRACTING FAILED")
    elif not flag_loader:
        print("FAILURE :LODING FAILED")



schedule.every().day.at("11:52").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)