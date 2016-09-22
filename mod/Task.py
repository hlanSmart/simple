#!/usr/bin/python
#coding:utf-8
from pkg.Conf import readYaml
from pkg.Hlan import main as hlan
from pkg.Hlan import OpArgs
import os 
def main(args):
    task_info=readYaml(os.path.abspath(args[2]))
    task_list=0
    if task_info:
        print('Task Group:%s\nTask List:'%task_info['group'])
        for i in task_info['task']:
            task_list+=1
            print('task%s:%s'%(task_list,i['name']))
            i.pop('name')
            args=OpArgs(i,task_info['group'])
            print(hlan(args))
        return ''
    else:
        return ''
        