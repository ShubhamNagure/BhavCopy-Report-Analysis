import  os
import django
import csv
from util.getData import get_filedate


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Project.settings')
django.setup()

from MainApp.models import BhavcopyRec


def main():
    filedate = get_filedate()
    filename= 'input.csv'
    path = f'F:/BhavCopy-Report-Analysis/BhavCopy-Report-Analysis/Project/util/data/{filedate}'
    print(path)
    os.chdir(path)
    with open(filename) as f:
        reader = csv.reader(f)
        for column in reader:
            _, created = BhavcopyRec.objects.update_or_create(
                sc_code=column[1],
                sc_name=column[2],
                sc_open=column[5],
                sc_high=column[6],
                sc_low=column[7],
                sc_close=column[8],
            )

if __name__ =='__main__':
    main()