import urllib.request
import socket

class IP:
    #you can change the url to get public IP
    def __init__(self, wan_url='https://ident.me'):
        self.lan_ip = self.get_lan_ip()
        self.wan_ip = self.get_wan_ip(wan_url)

    def get_lan_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(('10.255.255.255',1))
            IP = s.getsockname()[0]
        except:
            IP = '127.0.0.1'
        finally:
            s.close()
        return IP

    def get_wan_ip(self, wan_url):
        wan_ip = urllib.request.urlopen(wan_url).read().decode('utf8')
        return wan_ip