#!/home/shubham/BhavCopy-Report-Analysis/Project/venv/bin/python3
import getData
import insertoRedis
import os

import schedule
import time

#added this comment line to check github webhook working

def job():

    """ `STEP-1` : get data from site """
    flag=getData.handle_getDate()

    """ `STEP-2` : delete old and load new data """
    print(flag)
    if flag:
        insertoRedis.handle_WOR()
    else:
        print("INSERTION FAILED : cannot load data")

    #if flag and flag_loader:
    #    print("SUCCESS: Data EXTRACTED and LOADED Successfully !!!")
    #elif not flag:
    #    print("FAILURE :DOWNLOAD AND EXTRACTING FAILED")
    #elif not flag_loader:
    #    print("FAILURE :LODING FAILED")



schedule.every().monday.at("18:15").do(job)
schedule.every().tuesday.at("18:15").do(job)
schedule.every().wednesday.at("18:15").do(job)
schedule.every().thursday.at("18:15").do(job)
schedule.every().friday.at("18:15").do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
