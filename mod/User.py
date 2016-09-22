#!/usr/bin/python
#coding:utf-8
from pkg.File import isCreateFile,WriteFile

import datetime,time
def ValiddLogin():
    login_valid=isCreateFile('/tmp/hlan')
    if login_valid !='':
        if int(login_valid) > int(time.time()):
            return True
    return False
def Login(username=None,passwd=None):
    if username=='admin' and str(passwd)=='123456':
        WriteFile('/tmp/hlan', int(time.time())+ 600)
        return 'login vaild date:10m '
    else:
        return 'user or pass eroor!'
def main(args):
    return Login(args[2],args[3])
if __name__=='__main__':
    now = datetime.datetime.now()
    print(now)
    print()
