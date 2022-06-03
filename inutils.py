class datasets():
    
    class IpInfoIdentifiers():
    
    
        LookUpOpts =    ['ip',
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
            for i in range(len(datasets.IpInfoIdentifiers.LookUpOpts)):
                if DataType == datasets.IpInfoIdentifiers.LookUpOpts[i]:
                    return data[datasets.IpInfoIdentifiers.IpInfoLookupVals[i]]
                
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
    
    class base():
        
        class GetType():
            
            def encinputter(inp):
                import base64
                if inp == 64:
                    return base64.b64encode
                elif inp == 32:
                    return base64.b32encode
                elif inp == 16:
                    return base64.b16encode
                elif inp == 85:
                    return base64.b85encode
                
            def deencrypto(inp):
                import base64
                if inp == 64:
                    return base64.b64decode
                elif inp == 32:
                    return base64.b32decode
                elif inp == 16:
                    return base64.b16decode
                elif inp == 85:
                    return base64.b85decode
    
        def encode(txtstring:str,encinput:int):
            
            import base64,cryptography
            base = crypt.base.GetType.encinputter(encinput)(txtstring.encode('utf-8'))
            return str(base, "utf-8")
            
        def decode(txtstring:str,encinput:int):
            import base64
            base = crypt.base.GetType.deencrypto(encinput)(txtstring.encode('utf-8'))
            return str(base, "utf-8")
        
        
    
        
    
            

print('This file should not be run as a standalone script\nPlease import this file as \n"from inutils import ip"\nto use the functions of this file')if (__name__ =='__main__')else ('')
            
        
            
    
