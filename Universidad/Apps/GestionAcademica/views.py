# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.

def my_view(request, parameter):
    return HttpResponse("You're looking my view %s." % parameter)

def other_view(request, parameter):
    response = "You're looking other view %s."
    return HttpResponse(response % parameter)