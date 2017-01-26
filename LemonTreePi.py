#
#   Lemon Tree monitoring
#

import math
import time
from envirophat import light
from envirophat import weather

import os                                                                         #For the scp file copy    

def solar():
    
    sun_data = open("sun_%d_%d_%d.txt" %(year, month, day), "ab")

    l = light.light()

    if time.localtime()[4] == 15:
        sun = "%d.%d   %d" %(time.localtime()[3], time.localtime()[4]+10, l)        #This format allows me to import the txt file ...
    elif time.localtime()[4] == 30:                                                 #...to the Mac Grapher application
        sun = "%d.%d   %d" %(time.localtime()[3], time.localtime()[4]+20, l)        #These adjustments coorespond time to a corrext x-axis position
    elif time.localtime()[4] == 45:
        sun = "%d.%d   %d" %(time.localtime()[3], time.localtime()[4]+30, l)
    else:
        sun = "%d.%d   %d" %(time.localtime()[3], time.localtime()[4], l)           #when minutes = 0, no need to convert to coordiante      
        
    sun_data.write(sun)
    sun_data.write("\n")
    sun_data.close()
    os.system("scp %s owner1@192.168.0.102:~/Documents/LemonTreePi/Data_Text" %sun_data.name)       #sun_data not defined!!!!

    
    return sun


def temperature():  
    
    temp_data = open("temp_%d_%d_%d.txt" %(year, month, day), "ab") 

    fahrenheit = 1.8*(weather.temperature()-11)+32                                  #11 is a constant to account for the CPU temp difference

    temp = "%d   %d" %(time.localtime()[3], fahrenheit)

    temp_data.write(temp)
    temp_data.write("\n")
    temp_data.close()
    os.system("scp %s owner1@192.168.0.102:~/Documents/LemonTreePi/Data_Text" %temp_data.name)

    
    return temp





while True:                                                                         #runs constantly
    second = time.localtime()[5]
    minute = time.localtime()[4]         
    hour = time.localtime()[3]
    day = time.localtime()[2]
    month = time.localtime()[1]
    year = time.localtime()[0]
    
    if minute % 15 == 0 and second == 0:                                            #Records every 15 minutes
        solar()
        time.sleep(1)                                                               #Pause to prevent duplicate data
        
    if hour % 2 == 0 and minute == 0 and second == 3:                               #Records every 2 hours, after solar data is collected
        temperature()
        time.sleep(1)                                                               #Pause to prevent duplicate data
        




#This update:
#Once the function is invoked, it autoamtically sends (via scp) the file to the designated file path.
#The issue with having the file call outside of the function is that the file name is not defiend outside of the function.
#Keep an eye to see if temeprature will record, or if the scp takes more time than allocated

#Things to do:  Write Soil moisture sensor function
#               Optional: Have a report emailed every day as well

