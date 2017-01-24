import re
import os
import subprocess
import cx_Oracle
#cpath='/home/oms/oms/oracle'
def getdatafilecreationtime(cursor):
    fp=open('/home/oms/oms/oracle/monitor/oracle_command/getdatafilecreationtime.sql','r') 
    fp1=fp.read()
    s=cursor.execute(fp1)
    fp.close()
    row=s.fetchall()
    return row
def gettempusage(cursor):
    fp=open('/home/oms/oms/oracle/monitor/oracle_command/gettempusage.sql','r') 
    fp1=fp.read()
    s=cursor.execute(fp1)
    fp.close()
    row=s.fetchone()
    return row[0]
def getexecutions(cursor):
    fp=open('/home/oms/oms/oracle/monitor/oracle_command/getexecutions.sql','r') 
    fp1=fp.read()
    s=cursor.execute(fp1)
    fp.close()
    row=s.fetchall()
    return row

def check_active_session_count(cursor):
    cursor.execute('SELECT count(*) from v$session where status=\'ACTIVE\'')
    row=cursor.fetchone()
    return row[0]

def getunboundsql(cursor,unboundsql):
    fp=open('/home/oms/oms/oracle/monitor/oracle_command/getunboundsql.sql','r') 
    fp1=fp.read().strip()+unboundsql+'%\' order by last_load_time desc'
    s=cursor.execute(fp1)
    fp.close()
    row=s.fetchall()
    return row

def getanalyzedtime(cursor,table_name):
    fp1='SELECT owner,table_name,num_rows,sample_size,last_analyzed FROM DBA_TABLES WHERE  TABLE_NAME in ('+table_name+') order by table_name'
    s=cursor.execute(fp1)
    row=s.fetchall()
    return row

def getsegmentssize(cursor):
    #fp1='SELECT * FROM (SELECT OWNER,segment_name,SEGMENT_TYPE,TABLESPACE_NAME ,BYTES/1024/1024 FROM DBA_SEGMENTS  WHERE OWNER in('+owner+') ORDER BY BYTES DESC)WHERE ROWNUM<=20'
    fp1='SELECT OWNER,segment_name,SEGMENT_TYPE,TABLESPACE_NAME ,BYTES/1024/1024 FROM DBA_SEGMENTS WHERE BYTES/1024/1024>1024 ORDER BY BYTES DESC'
    s=cursor.execute(fp1)
    row=s.fetchall()
    return row
def getprocesstext(cursor,pid):
    fp1='select a.spid,b.sid,c.hash_value,substr(c.sql_text, 0, 40),b.logon_time,b.program from v$process a, v$session b, V$SQL c where a.addr = b.paddr and b.sql_hash_value = c.hash_value and a.spid in ('+pid+')'
    s=cursor.execute(fp1)
    row=s.fetchall()
    return row
def getprocessno(cursor,sid):
    fp1='select pro.spid from v$session ses,v$process pro where ses.sid='+sid+' and ses.paddr=pro.addr'
    s=cursor.execute(fp1)
    row=s.fetchone()
    if row is None:
	return 'None'
    else:
        return row[0]
if __name__ == '__main__':
    ipaddress='10.65.1.118'
    username='sys'
    password='ase_sys_1'
    port='1524'
    tnsname='HDB'
    try:
        db = cx_Oracle.connect(username+'/'+password+'@'+ipaddress+':'+port+'/'+tnsname ,mode=cx_Oracle.SYSDBA)
    except Exception , e:
        content= (tnsname+' is Unreachable,The reason is '+ str(e)).strip()
	print content
        #mailcontent.append(content)
    else:
        cursor = db.cursor()
	pid='9881'
        #j=check_mv_compile_states(cursor)
	row=getprocesstext(cursor,pid)
        cursor.close()
        db.close()
	print row















