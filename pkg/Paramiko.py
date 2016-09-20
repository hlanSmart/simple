#!/usr/bin/python
#coding:utf-8
import paramiko
class run_cmd():
    def __init__(self,hostname=None,password=None,username=None,port=None,echo_cmd=None):
        self.hostname=hostname
        self.password=str(password)
        self.username=username
        self.port=port
        self.echo_cmd=echo_cmd
    def run(self):
#         print self.echo_cmd,self.port,self.hostname,self.password
        paramiko.util.log_to_file('/tmp/paramiko.log')
        s=paramiko.SSHClient()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        res_dict={}
        try:
            s.connect(hostname = self.hostname,username=self.username, password=self.password,port=self.port)
            res_dict['status']='ok'
            stdin,stdout,stderr=s.exec_command(self.echo_cmd) 
            res_dict['value']=stdout.read()
            s.close()
        except Exception as e:
            res_dict['status']='error'
            res_dict['value']=e
        finally:
            return res_dict
class SFTP():
    def __init__(self,hostname=None,password=None,username=None,port=None):
        self.hostname=hostname
        self.port=port
        self.username=username
        self.password=password
        self.con()
    def con(self):
        try:
            t=paramiko.Transport((self.hostname,self.port))
            t.connect(username=self.username,password=self.password)
            self.sftp=paramiko.SFTPClient.from_transport(t)
        except Exception as e:
            print(e)
    def put(self,local_=None,remote_=None):
        try:
            self.sftp.put(local_,remote_)
            return dict(status='ok',value='put success!')
        except Exception as e:
            return dict(status='error',value=e)
    def get(self,remote_=None,local_=None):
        try:
            self.sftp.get(remote_,local_)
            return dict(status='ok',value='get success!')
        except Exception as e:
            return dict(status='error',value=e)
    def close(self):
        self.sftp.close()
if __name__=='__main__':
    test=SFTP(hostname='127.0.0.1',password='123456',username='root',port=22)
#     test.get('/etc/hosts', '/tmp/hosts')
    test.put('/etc/hosts', '/tmp/hosts')
    test.close()
        