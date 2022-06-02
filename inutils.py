from hashlib import sha256
from requests import request


class datasets():
    LookUpOpts = ['ip',
                    'region',
                    'city',
                    'organisation',
                    'rawlocation',
                    'postalcode',
                    'timezone',
                    'anycaststatus',
                    'country']
    
    IpInfoLookupVals =['ip',
                   'region',
                   'city',
                   'org',
                   'loc',
                   'postal',
                   'timezone',
                   'anycast',
                   'country']
class ip():
    
    def get():
        import requests
        ip = requests.get('https://api.ipify.org/').text
        return ip
    
    
    def lookup(ip,DataType=''):
        import requests
        data = requests.get(f'https://ipinfo.io/{ip}/json').json()
        data.pop('readme')
          
        if len(DataType) == 0:
            return data
        else:
            for i in range(len(datasets.LookUpOpts)):
                if DataType == datasets.LookUpOpts[i]:
                    return data[datasets.IpInfoLookupVals[i]]
                
    def ping(ip):
        import subprocess;from subprocess import DEVNULL
        return True if (subprocess.call(f'ping -n 1 {ip}',stdout=DEVNULL, stderr=subprocess.STDOUT) == 0) else False
    
    def HostToIp(host):
        
        import socket
        return socket.gethostbyname(host)
    
    def CheckPort(ip, port:int, tout =0.5):
        import socket
        from socket import timeout
        socket.setdefaulttimeout(tout)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((ip,port))
        s.close()
        return True if result ==0 else False
    
class crypt():
    
    class base64():
        
        def encode(txtstring:str):
            import base64,cryptography
            base = base64.b64encode(txtstring.encode('utf-8'))
            return str(base, "utf-8")
            
        def decode(txtstring:str):
            import base64
            base = base64.b64decode(txtstring.encode('utf-8'))
            return str(base, "utf-8")
            

print('This file should not be run as a standalone script\nPlease import this file as \n"from inutils import ip"\nto use the functions of this file')if (__name__ =='__main__')else ('')
            
        
            
    
