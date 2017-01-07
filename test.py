#
#   Lemon Tree monitoring
#

import math
import time
import threading

##
##def water():
##    n = 99
##    n = float(n)*float(.01)     #dummy line
##    return n
##


##def plant_diagnostic():
##    print "Water level is %s. The plant has recieved %d hours of sunlight" %(water(), solar())
##
##
##
##print time.localtime()[3]       #Gives the hour of that day! Ya!
##print plant_diagnostic()
##


#two time functions; one for the solar alone ( for averages) and the other for automation







#This lets me run the test constatly
#Can edit it to run every hour, several times an hour, etc.



from envirophat import light

def solar():
    
    data = open("sundata.txt.", "ab")

    light = light.light()

    sun = "At %d:%d, the plant has %d sunlight" %(time.localtime()[3], time.localtime()[4], light)
    
    data.write(sun)
    data.write("\n")
    data.close()
    
    return sun


print solar()


while True:                        #Endless loop
    a = time.localtime()[5]         #a is a minute counter, [5] deals in seconds, [4] in minutes
    if a % 15 == 0:                 #every 15 minutes (when seconds = 0)
        print solar()
        time.sleep(15)


        



