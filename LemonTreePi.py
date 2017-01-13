#
#   Lemon Tree monitoring
#

import math
import time
from envirophat import light
from envirophat import weather


def solar():
    
    sun_data = open("sundata_%d_%d_%d.txt" %(year, month, day), "ab")

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


def temperature():  #Need to calibrate this; it's reading CPU heat
    
    temp_data = open("tempdata_%d_%d_%d.txt" %(year, month, day), "ab") 

    fahrenheit = 1.8*(weather.temperature()-11)+32                             #11 is a constant to account for the CPU temp difference

    temp = "%d   %d" %(time.localtime()[3], fahrenheit)

    temp_data.write(temp)
    temp_data.write("\n")
    temp_data.close()

    return temp





while True:                                                                     #runs constantly
    second = time.localtime()[5]
    minute = time.localtime()[4]         
    hour = time.localtime()[3]
    day = time.localtime()[2]
    month = time.localtime()[1]
    year = time.localtime()[0]
    

#    if hour == 0: #This is probably not necessaryy                              #at the start of a new day...
#        sun_data = open("sundata_%d_%d_%d.txt" %(year, month, day), "ab")       #... create new files with the date
#        temp_data = open("tempdata_%d_%d_%d.txt" %(year, month, day), "ab")           #temperature data


    
    if minute % 15 == 0 and second == 0:                #Records every 15 minutes
        solar()
        time.sleep(1)                                   #Pause to prevent duplicate data
        
    if hour % 2 == 0 and minute == 0 and second == 3:   #Records every 2 hours, after solar data is collected
        temperature()
        time.sleep(1)                                   #Pause to prevent duplicate data
        



#This update:
#   Cleaned up a good bit of the code, and made the comments easier to understand
#   Hid the beggining-of-the-day loop (if hour == 0:), since the files should be created and opened properly when their functions are called anyways.
#       I will delete this once I'm sure it's not necessary
#   No duplicate data issues, which were caused by multiple 'nohup' executes in ther Terminal. (My bad)



#Things to do:  Calibrate temperature sensor. Use A/C readout, as well as candy termometer.
#                   Rewrite temperature function to accomodate
#               Write Soil moisture sensor function
#               Have the pi email me every day with the day's data (sun, temperature, soil status)
