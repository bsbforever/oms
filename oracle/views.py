#!/usr/bin/python
#coding=utf-8
import MySQLdb
import re
import os
#import cx_Oracle
#import redis
import time
import datetime
import MySQLdb
from django.views.decorators.http import require_http_methods
#from oracle.monitor.getoraclecommandresult import *
#from oracle.monitor.getoracleperformaceinfo import *
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpRequest
from django import template
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from oracle.models import *
from oracle.form import *
#from oracle.monitor.test import *
#from oracle.monitor.oracletopsql import *
#from oracle.monitor.highcharts_template import *
#from oracle.monitor.oracle_performance import *
from django.contrib.auth.models import User, Group



# Create your views here.

def index(request):
    result=oraclelist.objects.all().order_by('tnsname')
    dic={'result':result}
    return render_to_response('index.html',dic)

