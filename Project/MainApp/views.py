from django.shortcuts import render
from django.http import HttpResponse

from .models import *
from django.conf import settings
from django.contrib import messages
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt
from django.core.cache import cache
import csv
import io



def index(request):
    return render(request,'index.html')


CACHE_TTL = getattr(settings ,'CACHE_TTL' , DEFAULT_TIMEOUT)

def get_bhavcopy_rec(filter_rec = None):
    if filter_rec:
        print("DATA COMING FROM DB")
        rec = BhavcopyRec.objects.filter(sc_name__contains = filter_rec)
    else:
        rec = BhavcopyRec.objects.all()
    return rec


def home(request):
    filter_rec = request.GET.get('sc_name')
    if cache.get(filter_rec):
        print("DATA COMING FROM CACHE")
        rec = cache.get(filter_rec)
    else:
        if filter_rec:
            rec = get_bhavcopy_rec(filter_rec)
            cache.set(filter_rec, rec)
        else:
            rec = get_bhavcopy_rec()

    context = {'rec': rec}
    return render(request, 'index.html', context)

def upload(request):
    csv_file = f'F:/BhavCopy-Report-AnalysisBhavCopy-Report-Analysis' \
               f'/Project/util/data/{filedate}/input.csv'

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    print("Removing Old Data")
    BhavcopyRec.objects.all().delete()
    print("Adding Updated Data")
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = BhavcopyRec.objects.update_or_create(
            sc_code=column[0],
            sc_name=column[1],
            sc_open=column[4],
            sc_high=column[5],
            sc_low=column[6],
            sc_close=column[7],
        )
        context = {'Success' : 'File successfully uploaded'}
    return render(request, 'upload.html' , context)