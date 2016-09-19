#!/usr/bin/python
#coding:utf-8
import os,yaml
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def readServer(sg,sl=False):                #sg ServerGroup 服务器组 sl ServerList 组列表
    with open(os.path.join(BASE_PATH,'etc/server.yml'),'r') as f:
        server=yaml.load(f)
    if sl:                                  #当ServerList为真时返回组,而不是组信息
        li=[]
        for i in server:
            li.append(i)
        return li
    if sg in server:
        gp=server[sg]                       #gp group 服务器组信息
        for i in gp:                        #默认22端口在配置文件不存在,所以手动添加到返回结果
            if len(gp[i])<3:
                gp[i].append(22)
        return gp
    return False                            #Server Group 不存在时返回False
