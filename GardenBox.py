#
#   Potted Plant & Windowsill garden monitoring
#
import math
import time
import os
import sys
from envirophat import light, weather, analog

#takes the arguments from the nohup command
username = sys.argv[1]
ip = sys.argv[2]
directory = sys,argv[3]

os.system("nohup python ~/GardenBox/GardenBox.py &")        #Ignores the hangup signal, allowing it to operate without SSH active

#The 'solar' function measures the amount of sunlight the Pi, and therefore plant, recieves.
#The 'if' statements convert the current time to an appropriate coordiante on the x-axis.
#This ensures accurate graphical data.
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
    os.system("scp %s %s@%s:%s" %(sun_data.name, username, ip, directory))        
    
    return sun

#The 'temperature' function measures the temperature in Farenheit.  
#This function accomodates for the Enviro pHat measuring the CPU temperature and not the 'room temperature'.
#This function outputs the accurate air/room temperature.
def temperature():  
    
    temp_data = open("temp_%d_%d_%d.txt" %(year, month, day), "ab") 
    fahrenheit = 1.8*(weather.temperature()-11)+32                                  #11 is a constant to account for the CPU temp difference

    temp = "%d   %d" %(time.localtime()[3], fahrenheit)

    temp_data.write(temp)
    temp_data.write("\n")
    temp_data.close()
    os.system("scp %s %s@%s:%s" %(temp_data.name, username, ip, directory))   

    return temp

#The 'soil_mositure' function takes data from the soil moisture sensors that can be attached to the Enviro pHat.
#The minimum out is '0', with means no water is present.  The maximum output is '5', which means full-saturation (obtained by fully submerging in water).
#I have two soil moisture sensors in my current plant; each one takes a separate reading, 
#and this function writes both out to a text file, as well as an average.  If you only want to use one sensor, 
#only one 'analog.read()' needs to be implemented, and 'avg_moisture' reading can be deleted.
#If you do use a different amount of soil sensors, make sure to remove the extra write calls from the 'moisture' variable
def soil_moisture():
    
    soil_data = open("moist_%d_%d_%d.txt" %(year, month, day), "ab")
    avg_moisture = (analog.read(0) + analog.read(1))/2
    
    moisture = "%d   %f    %f  %f" %(time.localtime()[3], avg_moisture, analog.read(0), analog.read(1))
    
    soil_data.write(moisture)
    soil_data.write("\n")
    soil_data.close()
    os.system("scp %s %s@%s:%s" %(soil_data.name, username, ip, directory))  

    return moisture

while True:                                                                         
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
#User, IP, and directory are now specifed during nohup

#Things to do: 
#               Optional: Have a report emailed every day as well
