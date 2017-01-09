#
#   Lemon Tree monitoring
#

import math
import time
import threading


##def plant_diagnostic():
##    print "Water level is %s. The plant has recieved %d hours of sunlight" %(water(), solar())



from envirophat import light



def solar():
    
    sun_data = open("sundata_%d_%d_%d.txt" %(year, month, day), "ab")

    l = light.light()


    sun = "%d.%d   %d" %(time.localtime()[3], time.localtime()[4], l)       #This format allows me to import the txt file to the Grapher application
    
    sun_data.write(sun)
    sun_data.write("\n")
    sun_data.close()
    
    return sun


#print solar()


while True:                                                                 #runs constantly
    minute = time.localtime()[4]         
    hour = time.localtime()[3] 
    year = time.localtime()[0]
    month = time.localtime()[1]
    day = time.localtime()[2]

    if hour == 0:                                                           #at the start of a new day...
        sun_data = open("sundata_%d_%d_%d.txt" %(year, month, day), "ab")       #... create a new file with the date

    
    if minute % 15 == 0:                 #every 15 minutes 
        print solar()
        time.sleep(60)                      #to prevent duplicate data


        



#This latest update now creates a new file to store the solar data in at the beginning of each day.
#Also, the light data is now in a form that can be imported by Grapher
