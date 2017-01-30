#
#   Lemon Tree monitoring
#
import math
import time
import os                                                                            
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
    os.system("scp %s owner1@192.168.0.102:~/Documents/LemonTreePi/Data_Text" %sun_data.name)        #Change to desired computer name, IP, and Directory
    
    return sun

def temperature():  
    
    temp_data = open("temp_%d_%d_%d.txt" %(year, month, day), "ab") 

    fahrenheit = 1.8*(weather.temperature()-11)+32                                  #11 is a constant to account for the CPU temp difference

    temp = "%d   %d" %(time.localtime()[3], fahrenheit)

    temp_data.write(temp)
    temp_data.write("\n")
    temp_data.close()
    os.system("scp %s owner1@192.168.0.102:~/Documents/LemonTreePi/Data_Text" %temp_data.name)   #Change to desired computer name, IP, and Directory

    return temp

def soil_moisture():
    
    soil_data = open("moist_%d_%d_%d.txt" %(year, month, day), "ab")
    avg_moisture = (analog.read(0) + analog.read(1) + analog.read(2))/3
    
    moisture = "%d   %f    %f  %f  %f" %(time.localtime()[3], avg_moisture, analog.read(0), analog.read(1), analog.read(2))
    
    soil_data.write(moisture)
    soil_data.write("\n")
    soil_data.close()
    os.system("scp %s owner1@192.168.0.102:~/Documents/LemonTreePi/Data_Text" %soil_data.name)  #Change to desired computer name, IP, and Directory

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
        time.sleep(1)                                                               #Pause to prevent duplicate data
        
    if hour % 2 == 0 and minute == 0 and second == 30:                               #Records every 2 hours, after solar data is collected
        temperature()
        soil_moisture()
        time.sleep(1)                                                               #Pause to prevent duplicate data
    
    time.sleep(0.5)                                                                 #To prevent CPU from running at 99.9%

#This update:
#Changed Temeprature to collect every two hours when minute = 1: this should still collect data incase the fiel copy (scp) stumbles
#Added the soil_mositure sensor functionality.  It will take data readings from three sensors, as well as an average, every 2 hours
#Added a sleep timer to try and prevent the CPU running at 99.9% constantly

#Things to do: 
#               Optional: Have a report emailed every day as well
