from django.shortcuts import render

from .models import *
from django.conf import settings
from django.contrib import messages
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt
from django.core.cache import cache



CACHE_TTL = getattr(settings ,'CACHE_TTL' , DEFAULT_TIMEOUT)

def get_bhavcopy_rec(filter_rec = None):
    if filter_rec:
        print("DATA COMING FROM DB")
        rec = BhavcopyRec.objects.filter(sc_name__contains = filter_rec)
    else:
        rec = BhavcopyRec.objects.all()
    return rec


def home(request):
    filter_rec = request.GET.get('stock')
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

