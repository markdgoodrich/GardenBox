#
#   Lemon Tree monitoring
#

import math
import time
import os                                                                         #For the scp file copy    
from envirophat import light, weather, analog

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


#This si teh prototype soil mositure sensor
#analog.read(0), analog.read(1), analog.read(2) are currently plugged into the Lemon Tree
#I believe the sensors max out at a reading of around 4.2 (when submersed in water)
#They register 0 when removed from water, and are just in air
#I will do research on the proepr saturation for a Lemon Tree

def soil_moisture():
    soil_data = open("moist_%d_%d_%d.txt" %(year, month, day), "ab")
    avg_moisture = (analog.read(0) + analog.read(1) + analog.read(2))/3
    
    moisture = "%d   %d" %(time.localtime()[3], avg_moisture)
    
    soil_data.write(moisture)
    soil_data.write("/n")
    soil_data.close()
    os.system("scp %s owner1@192.168.0.102:~/Documents/LemonTreePi/Data_Text" %soil_data.name)

    return moisture


while True:                                                                         #runs constantly
    second = time.localtime()[5]
    minute = time.localtime()[4]         
    hour = time.localtime()[3]
    day = time.localtime()[2]
    month = time.localtime()[1]
    year = time.localtime()[0]
    
    if minute % 15 == 0 and second == 0:                                            #Records every 15 minutes
        solar()
        soil_moisture()         #Move this down to every several hours, once testing is done
        time.sleep(1)                                                               #Pause to prevent duplicate data
        
    if hour % 2 == 0 and minute == 1 and second == 0:                               #Records every 2 hours, after solar data is collected
        temperature()
        time.sleep(1)                                                               #Pause to prevent duplicate data
        




#This update:
#Changed Temeprature to colelct every two hours when minute = 1: this should still colelct data then if the scp takes a long time
#Added the soil_mositure sensor functionality.  I will eventually have it record less often then every 15 minutes

#Things to do: 
#               Optional: Have a report emailed every day as well
