#
#   Lemon Tree monitoring
#

import math
import time
import threading


##def plant_diagnostic():
##    print "Water level is %s. The plant has recieved %d hours of sunlight" %(water(), solar())



from envirophat import light
from envirophat import weather



def solar():
    
    sun_data = open("sundata_%d_%d_%d.txt" %(year, month, day), "ab")

    l = light.light()

    if time.localtime()[4] == 15:
        sun = "%d.%d   %d" %(time.localtime()[3], time.localtime()[4]+10, l)       #This format allows me to import the txt file to the Grapher application
    elif time.localtime()[4] == 30:
        sun = "%d.%d   %d" %(time.localtime()[3], time.localtime()[4]+20, l)        #These adjsutments coorespond time to a corrext x-axis position
    elif time.localtime()[4] == 45:
        sun = "%d.%d   %d" %(time.localtime()[3], time.localtime()[4]+30, l)
    else:
        sun = "%d.%d   %d" %(time.localtime()[3], time.localtime()[4], l)           #when minutes = 0 , new hour      
        
    sun_data.write(sun)
    sun_data.write("\n")
    sun_data.close()
    
    return sun




def temperature():
    
    temp_data = open("tempdata_%d_%d_%d.txt" %(year, month, day), "ab") #year, month, day variables

    fahrenheit = 1.8*float(weather.temperature())+32

    temp = "%d   %d" %(time.localtime()[3], fahrenheit)

    temp_data.write(temp)
    temp_data.write("\n")
    temp_data.close()

    return temp






while True:                                                                 #runs constantly
    second = time.localtime()[5]
    minute = time.localtime()[4]         
    hour = time.localtime()[3]
    day = time.localtime()[2]
    month = time.localtime()[1]
    year = time.localtime()[0]
    

    if hour == 0:                                                           #at the start of a new day...
        sun_data = open("sundata_%d_%d_%d.txt" %(year, month, day), "ab")       #... create new files with the date
        temp_data = open("tempdata_%d_%d_%d.txt" %(year, month, day), "ab")            #temperature data


    
    if minute % 15 == 0 and second == 0:                 #every 15 minutes 
        solar()
        time.sleep(.1)                                   #to prevent duplicate data

#----Below is a rough execution of the temperature test every 12 hours------#

    if hour % 2 == 0 and second == 3:           #The idea is that, every two hours, on the first second, this will excecute once
        temperature()
        time.sleep(.1)
        



#This latest update now creates a new file to store the solar data in at the beginning of each day.
#Also, the light data is now in a form that can be imported by Grapher.  This includes proper adjsut of time to x-axis coordinates
# A commented-out section of the Temperature sensor is included, but I want to ensure that the solar function is solid before implementing 
