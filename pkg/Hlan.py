#!/usr/bin/python
#coding:utf-8
def main(args):
    load_mod=__import__(args[1])
    res=load_mod.main(args)
    return res
def OpArgs(d,g):
    for i in d:
        s=d[i]
        li=['hlan',i,g]
        if '!' in s:
            arg=[s.replace('!','')]
        else:
            arg=s.split(' ')
        li+=arg
    return li