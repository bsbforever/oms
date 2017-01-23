#!/usr/bin/python
#coding=utf-8
import MySQLdb
import re
import os
import cx_Oracle
#import redis
import time
import datetime
from django.views.decorators.http import require_http_methods
from oracle.monitor.getoraclecommandresult import *
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


def oracle_command(request):
    result=oraclelist.objects.all().order_by('tnsname')
    dic={'result':result}
    return render_to_response('oracle_command.html',dic)


def commandresult(request):
    ipaddress  = str(request.GET['ipaddress']).split('-')[0]
    tnsname=str(request.GET['ipaddress']).split('-')[1]
    command_content  = str(request.GET['operate'])
    result=oraclelist.objects.all().order_by('tnsname')
    for i in result:
        if i.ipaddress==ipaddress:
            username =i.username
            password=i.password
            port=i.port
            break
    if command_content=='check_session_count':
        try:
            db = cx_Oracle.connect(username+'/'+password+'@'+ipaddress+':'+port+'/'+tnsname ,mode=cx_Oracle.SYSDBA)
        except Exception , e:
            content= (ipaddress+' is Unreachable,The reason is '+ str(e)).strip()
            return HttpResponse(content)
        else:
            cursor = db.cursor()
            row=check_active_session_count(cursor)
            cursor.close()
            db.close()
            return HttpResponse(row)
    elif command_content=='check_datafile_time':
        try:
            db = cx_Oracle.connect(username+'/'+password+'@'+ipaddress+':'+port+'/'+tnsname ,mode=cx_Oracle.SYSDBA)
        except Exception , e:
            content= (ipaddress+' is Unreachable,The reason is '+ str(e)).strip()
            return HttpResponse(content)
        else:
            cursor = db.cursor()
            row=getdatafilecreationtime(cursor)
            cursor.close()
            db.close()
            title='数据文件创建时间-'+ipaddress+'-'+tnsname
            tr=['数据文件名称','文件大小','表空间','自动扩展','创建时间']
            dic ={'title':title,'tr':tr,'row':row}
            #return render_to_response('oracle_command_result1.html',dic)
            return HttpResponse(dic)

