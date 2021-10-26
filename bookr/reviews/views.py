from django.shortcuts import render
from django.http import HttpResponse
import logging
from django.conf import settings
import json


def index(request):
    name = request.GET.get('name') or 'none'
    dic = {'name': name, }
    if settings.DEBUG:
        logging.debug(request.GET)
    return render(request, 'base.html', dic)


def book_search(request):
    terms = {'search': request.GET.getlist('search')[0], }
    logging.debug(terms.values())
    return render(request, 'search.html', terms)


