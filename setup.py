#En este proyecto se van localizar la ip introducida y tambien se van a implementar diferentes herramientas
import time
import os
import pygeoip
import socket
from virus_total_apis import PublicApi
import urllib
import urllib.request
from hashlib import md5
import py2exe

gi = pygeoip.GeoIP("C:/Users/viruz/Desktop/ESCRITORIO/Github/Python/PythonIp/GeoLiteCity.dat")

API_KEY = "[a628ffa355c2eee5ac6ba7a9b94a8e6b2c2c9ce737ac7a22762ad4488f8c6628]"
api = PublicApi(API_KEY)
#Funciones

def inicio():
    print("                                                 ")
    print("                                                 ")
    print("  _____       _     _              _____         ")
    print(" |  __ \     | |   | |            |_   _|        ")
    print(" | |__) |   _| |__ | |_ ___  _ __   | |  _ __    ")
    print(" |  ___/ | | | '_ \| __/ _ \| '_ \  | | | '_ \   ")
    print(" | |   | |_| | | | | || (_) | | | |_| |_| |_) |  ")
    print(" |_|    \__, |_| |_|\__\___/|_| |_|_____| .__/   ")
    print("         __/ |                          | |      ")
    print("        |___/                           |_|      ")
    print("                                                 ")
def Metodo1():
    ip = input("Ingresa la ip a geolocalizar: ")
    printinfo(ip)
def informacion():
    inicio()
    print("-----------------------------------------------------------")
    obtener_hostname()
    getip = IP()
    print("Public Ip: ", getip.lan_ip)
    print("Private Ip: ", getip.wan_ip)
    date_time()
    print("-----------------------------------------------------------")
def date_time():
    time.strftime('%Y-%m-%d %H:%M', time.localtime())
    print(time.strftime('%Y-%m-%d %H:%M', time.localtime()))
def printinfo(ip):
    rec = gi.record_by_name(ip)
    city = rec['city']
    country = rec['country_name']
    longitude = rec['longitude']
    lat = rec['latitude']
    print('[*] Direccion Ip: '  + ip + ' geocalizada ')
    print('[*] ' +str(city)+ ', '+str(country))
    print('[*] Latitud: ' +str(lat)+ ', Longitud: '+ str(longitude))
def obtener_hostname():
    nombre_equipo = socket.gethostname()
    direccion_equipo = socket.gethostbyname(nombre_equipo)
    print("HostName: %s" % nombre_equipo)




#Clases

class IP:                                                            #Creditos a https://github.com/paulcaro
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

#Codigo

inicio()

print("Hola, te damos la bienvenida a PythonIp esta herramienta te ayudara a acceder facilmente a la informacion de una Ip, URL o un Archivo")

opcionales1 = input("Seleccione una opcion:\n\nA)Metodo-1 B)Metodo-1-Graphic C)VirusTotal\n\nInserte la letra en Mayuscula: ")

if opcionales1 == "A":
    os.system("cls")
    informacion()
    Metodo1()
elif opcionales1 == "B":
    os.system("python main.py")
elif opcionales1 == "C":
    print("Esta herramienta esta en desarrollo")
else:
    SystemError
