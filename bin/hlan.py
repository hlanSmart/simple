#!/usr/bin/python
#coding:utf-8
import os,sys
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD_DIR=os.path.join(BASE_PATH,'mod')
sys.path.append(BASE_PATH)
sys.path.append(MOD_DIR)
from mod.User import ValiddLogin
from pkg.Hlan import main
if __name__=='__main__':
    if ValiddLogin() or sys.argv[1]=='User':
            print(main(sys.argv))
    else:
        print('no login,please excute: \n python hlan.py User admin 123456')
#     try:
#         if ValiddLogin() or sys.argv[1]=='User':
#             print(main(sys.argv))
#         else:
#             print('no login,please excute: \n python hlan.py User admin 123456')
#     except Exception as e:
#         print(e)
#         main(['','Help'])