import os 
import django
from getData import get_filedate

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Project.settings')
django.setup()
from MainApp.models import BhavcopyRec
import csv

fileDate = str(get_filedate())


file_handle = open(f"util/data/041121/inputRedis.csv", "r", encoding="utf-8")
reader = csv.reader(file_handle)
next(reader)
for row in reader:
    
    created = BhavcopyRec.objects.create(
        sc_code=row[0],
        sc_name=row[1],
        sc_open=row[2],
        sc_high=row[3],
        sc_low=row[4],
        sc_close=row[5],
        sc_prevclose=row[6],
        sc_no_of_trades=row[7],
        sc_no_of_shares=row[8],
        sc_net_turnover=row[9],
        report_date=fileDate

        )
    
    created.save()
    print('this row is printing',row)
    # except:
    #     print ("there was a problem with line", row )