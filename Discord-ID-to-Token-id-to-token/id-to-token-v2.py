# Modules importation
import os
import base64
import datetime
import time

try:
    from colorama import Fore, init
except:
    os.system("py -m pip install colorama")
    from colorama import Fore, init
init()

banner = (Fore.MAGENTA + """
  ██▓▓█████▄    ▄▄▄█████▓ ▒█████     ▄▄▄█████▓ ▒█████   ██ ▄█▀▓█████  ███▄    █
 ▓██▒▒██▀ ██▌   ▓  ██▒ ▓▒▒██▒  ██▒   ▓  ██▒ ▓▒▒██▒  ██▒ ██▄█▒ ▓█   ▀  ██ ▀█   █
 ▒██▒░██   █▌   ▒ ▓██░ ▒░▒██░  ██▒   ▒ ▓██░ ▒░▒██░  ██▒▓███▄░ ▒███   ▓██  ▀█ ██▒
 ░██░░▓█▄   ▌   ░ ▓██▓ ░ ▒██   ██░   ░ ▓██▓ ░ ▒██   ██░▓██ █▄ ▒▓█  ▄ ▓██▒  ▐▌██▒
 ░██░░▒████▓      ▒██▒ ░ ░ ████▓▒░     ▒██▒ ░ ░ ████▓▒░▒██▒ █▄░▒████▒▒██░   ▓██░
 ░▓   ▒▒▓  ▒      ▒ ░░   ░ ▒░▒░▒░      ▒ ░░   ░ ▒░▒░▒░ ▒ ▒▒ ▓▒░░ ▒░ ░░ ▒░   ▒ ▒
  ▒ ░ ░ ▒  ▒        ░      ░ ▒ ▒░        ░      ░ ▒ ▒░ ░ ░▒ ▒░ ░ ░  ░░ ░░   ░ ▒░
  ▒ ░ ░ ░  ░      ░      ░ ░ ░ ▒       ░      ░ ░ ░ ▒  ░ ░░ ░    ░      ░   ░ ░
  ░     ░                    ░ ░                  ░ ░  ░  ░      ░  ░         ░
""" + Fore.LIGHTCYAN_EX)

v2 = (Fore.RED+ "                       https://github.com/Walkoud                    v2 by Walkoud"+ Fore.LIGHTCYAN_EX)

print(banner, v2)
userid = input(" [INPUT] USER ID : ")
dateinput = input(" [INPUT] Date of the account created (16/07/2019, H:M:S) : ")



encodedBytes = base64.b64encode(userid.encode("utf-8"))
encodedStr = str(encodedBytes, "utf-8")

firstdate = dateinput.split(" ")[0]
secondeTime = dateinput.split(" ")[1]

date = firstdate.split("/")
time = secondeTime.split(":")

date_format = datetime.datetime.strptime(dateinput, "%d/%m/%Y, %H:%M:%S")
unix_timestamp = datetime.datetime.timestamp(date_format)


operation = str(int(unix_timestamp) - 1293840000)
encodedBytes2 = base64.b64encode(operation.encode("utf-8"))
encodedStr2 = str(encodedBytes2, "utf-8")



print(f'\n [LOGS] TOKEN FIRST AND SECOND PART : {encodedStr}.{encodedStr2}')




os.system('pause >nul')  # Pause command in Batch (press any key to exit the code)


#Discord : Walkoud#1981
#Discord : https://walkoud.carrd.co/