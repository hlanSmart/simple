#!/usr/bin/python
#coding:utf-8
from pkg.Paramiko import run_cmd
from pkg.Conf import readServer
import threading
def mod_help():
    pass
def execCmd(ip,v,g,rs=True):
    global mod_json
    rs=run_cmd(hostname=ip,password=v[1],username=v[0],port=v[2],echo_cmd=g)
    res=rs.run()
    mod_json[ip]=res
#     if rs:
#         for i in res['value']:
#             print('%s:\n%s' %(res['ip'],bytes.decode((res['value'][i]))))
#     else:
#     print(res)
#     print('ip:%s') % (res['ip'])
#     print('status:%s')%(res['status'])
#     if res['status']=='ok':
#         for y in res['value']:
#             print('command:%s\n%s')%(y,res['value'][y])

def main(argvs):
    global mod_json
    mod_json={}
#     print(argvs)
    server_list=readServer(argvs[2])
    g=argvs[3]
    T_thread=[]
    for (server,v) in server_list.items():
        t=threading.Thread(target=execCmd,args=(server,v, g))
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
    return mod_json