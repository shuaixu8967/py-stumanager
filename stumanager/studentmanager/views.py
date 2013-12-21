# -*- coding: utf-8 -*-
# Create your views here.
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
    return HttpResponse("Hello world")