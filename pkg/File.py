#!/usr/bin/python
#coding:utf-8

import os

def isCreateFile(P):
    if os.path.exists(P):
        with open(P) as f:
            return f.read()
    else:
        with open(P,'w') as f:
            f.write('')
        return isCreateFile(P)
def WriteFile(P,S):
    isCreateFile(P)
    with open(P,'w') as f:
        f.write(str(S))