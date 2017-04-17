import sys
import os

print"----------------------------------"
print"----------  GardenBox  -----------"
print"----------------------------------\m"
print "    Data Recording Setup\n"



username = raw_input("Enter your username (ex. owner1): ")
ip = raw_input("Enter the IP address (ex. 192.168.0.XXX): ")
location = raw_input("Enter exported data location (ex. ~/Documents): ")

os.system("nohup python GardenBox.py %s %s %s &" %(username, ip, location))
