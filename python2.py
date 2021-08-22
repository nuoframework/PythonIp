import json
import marshal
import pickle
import os
from virus_total_apis import PublicApi
from hashlib import md5

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

os.system("cls")
inicio()

opcionales2 = input("Inserte la Opcion deseada:\n\nA)Escanear Archivo  B)Escanear URL  C)Escanear Ip  D)Dominio\n\nInserte la letra en Mayuscula: ")

with open("response.json", "w") as f:
    json.dump(response, f, indent=4)


API_KEY = "[a628ffa355c2eee5ac6ba7a9b94a8e6b2c2c9ce737ac7a22762ad4488f8c6628]"
api = PublicApi(API_KEY)

def archivos():
    with open("ScanThis.pdf", "rb") as f:
        file_hash = md5(f.read()).hexdigest()
    response = api.get_file_report(file_hash)
    if response["response_code"] == 200:
        if response["results"]["positives"] > 0:
            print("Archivo malicioso.")
        else:
            print("Archivo seguro.")
    else:
        print("No ha podido obtenerse el análisis del archivo.")
    with open("response.json", "w") as f:
        json.dump(response, f, indent=4)

def url1():
    response = api.get_url_report("http://recursospython.com/")

def url2():
    response = api.scan_url("http://recursospython.com/")

def domino():
    response = api.get_domain_report("google.com")

def Ip():
    with open("ScanThis.pdf", "rb") as f:
        file_hash = md5(f.read()).hexdigest()
    response = api.get_ip_report("109.107.97.75")
    if response["response_code"] == 200:
        if response["results"]["positives"] > 0:
            print("Ip maliciosa.")
        else:
            print("Ip segura.")
    else:
        print("No ha podido obtenerse el análisis de la Ip.")


if opcionales2 == "A":
    archivos()
elif opcionales2 == "B":
    url2()
elif opcionales2 == "C":
    Ip()
elif opcionales2 == "D":
    domino()
else:
    SystemError