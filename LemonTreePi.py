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
    
    return sun


def temperature():  
    
    temp_data = open("temp_%d_%d_%d.txt" %(year, month, day), "ab") 

    fahrenheit = 1.8*(weather.temperature()-11)+32                                  #11 is a constant to account for the CPU temp difference

    temp = "%d   %d" %(time.localtime()[3], fahrenheit)

    temp_data.write(temp)
    temp_data.write("\n")
    temp_data.close()

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
        

    if hour == 7 and minute== 4 and second == 59:                               #Before midnight each day, copy data to specified directory
        os.system("scp %s owner1@192.168.0.101:~/Documents/LemonTreePi/Data_Text" %(sun_data.name))
        os.system("scp %s owner1@192.168.0.101:~/Documents/LemonTreePi/Data_Text" %(temp_data.name))



#This update:
#   Cleaned up a good bit of the code, and made the comments easier to understand
#   Temperature sensor is calibrated to give non-CPU heat
#   Changed file names from "sumdata_X_X_X" to "sun_X_X_X"
#   Figured out permissions to let pi scp to Mac without password (not coded here)
#   To make file transfer work: must have port 22 active (instructables.com/answers/Port-22-Connection-refused-using-ssh-remote-a) [x]
#   Must generate keys & share public with host ocmputer [x]           
#Currently commented out is the section that, before midnight each day, will copy the data files to a specified computer & directory on the local system


#Things to do:  Write Soil moisture sensor function
#               Optional: Have a report emailed every day as well

