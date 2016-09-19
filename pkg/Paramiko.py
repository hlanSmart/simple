#!/usr/bin/python
#coding:utf-8
import paramiko,datetime,os
class run_cmd():
    def __init__(self,hostname=None,password=None,username=None,port=None,echo_cmd=None):
        self.hostname=hostname
        self.password=password
        self.username=username
        self.port=port
        self.echo_cmd=echo_cmd
        self.thread_stop=False
    def run(self):
        print self.echo_cmd,self.port,self.hostname,self.password
        paramiko.util.log_to_file('/tmp/paramiko.log')
        s=paramiko.SSHClient()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        res_dict={}
        print(self.echo_cmd)
        s.connect(hostname = self.hostname,username=self.username, password=self.password,port=self.port)
        res_dict['status']='ok'
            
        res_dict['value']=stdin,stdout,stderr=s.exec_command(self.echo_cmd)
        s.close()
#         try:
#             s.connect(hostname = self.hostname,username=self.username, password=self.password,port=self.port)
#             res_dict['status']='ok'
#             
#             res_dict['value']=stdin,stdout,stderr=s.exec_command(self.echo_cmd)
#             s.close()
#         except Exception as e:
#             res_dict['status']='error'
#             res_dict['value']={'error':e}
#         finally:
#             return res_dict
class upload_sftp():
    def __init__(self,hostname=None,password=None,username=None,port=None,local_dir=None,remote_dir=None):
        self.hostname=hostname
        self.port=port
        self.username=username
        self.password=password
        self.local_dir=local_dir
        self.remote_dir=remote_dir
    def run(self):
        try:
            t=paramiko.Transport((self.hostname,self.port))
            t.connect(username=self.username,password=self.password)
            sftp=paramiko.SFTPClient.from_transport(t)
#             print self.remote_dir,self.local_dir
            sftp.put(self.local_dir,self.remote_dir)
            t.close()
#             print os.path.join(self.local_dir,f),os.path.join(self.remote_dir,'f')
#             try:
#                 sftp.put(self.local_dir,self.remote_dir)
#                 print('upload file finally %s ')% datetime.datetime.now()
#             except Exception as e:
#                 print(e)
            
#             for root,dirs,files in os.walk(self.local_dir):
#                 for filespath in files:
#                     local_file = os.path.join(root,filespath)
#                     a = local_file.replace(self.local_dir,self.remote_dir)
#                     remote_file = os.path.join(self.remote_dir,a)
#                     try:
#                         sftp.put(local_file,remote_file)
#                     except Exception as e:
#                         sftp.mkdir(os.path.split(remote_file)[0])
#                         sftp.put(local_file,remote_file)
#                     print("upload %s to remote %s")% (local_file,remote_file)
#                 for name in dirs:
#                     local_path = os.path.join(root,name)
#                     a = local_path.replace(self.local_dir,self.remote_dir)
#                     remote_path = os.path.join(self.remote_dir,a)
#                     try:
#                         sftp.mkdir(remote_path)
#                         print("mkdir path %s")% remote_path
#                     except Exception as e:
#                         print(e)
#                     print('upload file success %s ') % datetime.datetime.now()
#                     t.close()
        except Exception as e:
            print(e)
class get_sftp():
    def __init__(self,hostname=None,password=None,username=None,port=None,local_dir=None,remote_dir=None):
        self.hostname=hostname
        self.port=port
        self.username=username
        self.password=password
        self.local_dir=local_dir
        self.remote_dir=remote_dir
        self.thread_stop=False
    def run(self):
        try:
            t=paramiko.Transport((self.hostname,self.port))
            t.connect(username=self.username,password=self.password)
            sftp=paramiko.SFTPClient.from_transport(t)
            print('get file start %s ') % datetime.datetime.now()
            for root,dirs,files in os.walk(self.remote_dir):
                for name in dirs:
                    remote_path = os.path.join(root,name)
                    a = remote_path.replace(self.remote_dir,self.local_dir)
                    local_path = os.path.join(self.local_dir,a)
                    try:
                        sftp.mkdir(local_path)
                        print("mkdir path %s")% local_path
                    except Exception as e:
                        print(e)
                for filespath in files:
                    remote_file = os.path.join(root,filespath)
                    a = remote_file.replace(self.remote_dir,self.local_dir)
                    local_file = os.path.join(self.local_dir,a)
                    try:
                        sftp.get(remote_file,local_file)
                    except Exception as e:
                        sftp.mkdir(os.path.split(local_file)[0])
                        sftp.get(remote_file,local_file)
                    print("get %s to remote %s") % (remote_file,local_file)
            print('get file success %s ') % datetime.datetime.now()
            t.close()
        except Exception as e:
            print(e)