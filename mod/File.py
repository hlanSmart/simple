#!/usr/bin/python
#coding:utf-8
from pkg.Paramiko import SFTP
from pkg.Conf import readServer
from pkg.File import isCreateDir
import threading,os
def putFile(ip,v,local_,remote_):
    sftp=SFTP(hostname=ip,password=str(v[1]),username=v[0],port=v[2])
    mod_json[ip]=sftp.put(local_, remote_)
def getFile(ip,v,remote_,local_):
    isCreateDir(os.path.join(os.path.dirname(local_),ip))
    local_=os.path.join(os.path.join(os.path.dirname(local_),ip),os.path.basename(local_))
    sftp=SFTP(hostname=ip,password=str(v[1]),username=v[0],port=v[2])
    mod_json[ip]=sftp.get(remote_, local_)
def main(argvs):
    global mod_json
    mod_json={}
#     print(argvs)
    server_list=readServer(argvs[3])
    g=argvs[3]
    T_thread=[]
    for (server,v) in server_list.items():
        if argvs[2]=='get':
            t=threading.Thread(target=getFile,args=(server,v, argvs[4],argvs[5]))
        elif argvs[2]=='put':
            t=threading.Thread(target=putFile,args=(server,v, argvs[4],argvs[5]))
        else:
            print('''get-file:\tpython hlan.py File get server-group Remote-Path\nput-file:\tpython hlan.py File put server-group local_file remote_file''')
            exit()
        T_thread.append(t)
    for i in range(len(T_thread)):
        t.setDaemon(True)
        T_thread[i].start()
    for i in range(len(T_thread)):
        fina_flag=True
        if T_thread[i].is_alive():
            while fina_flag:
                if T_thread[i].is_alive():
                    continue
                else:
                    fina_flag=False
    res=''               
    for i in mod_json:
        res+='\n%s\t%s:\n%s' % (i,mod_json[i]['status'],mod_json[i]['value'])
    return res