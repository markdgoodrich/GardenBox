# GardenBox 
-------------

A simple monitoring system for your potted plants and windowsill gardens that will track & record: 

* Soil Moisture Levels
* Air Temperature
* Received Sunlight


This system uses [RaspberryPi](https://www.raspberrypi.org/products/), the Pimoroni [Enviro pHat](https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-enviro-phat), and SparkFun's [Soil Moisture Sensor](https://learn.sparkfun.com/tutorials/soil-moisture-sensor-hookup-guide).

----------------------
All collected data is copied and updated to a computer & destination designated by the user.  
To ensure quick and non-interupted data transfer, make sure to authenticate a [key](http://support.modwest.com/content/20/90/en/how-do-i-get-ssh-to-authenticate-me-via-publicprivate-keypairs-instead-of-by-password.html) from the Pi to your computer.


All data collected is automatically written and copied in a format that is compatible with the Mac OS X [Grapher](https://en.wikipedia.org/wiki/Grapher) application, making visual [solar](https://cloud.githubusercontent.com/assets/24979274/22472192/80b9fe48-e79a-11e6-984f-67acee63cab2.jpg), [moisture](https://cloud.githubusercontent.com/assets/24979274/22472191/80a2ccf0-e79a-11e6-8a2e-6bdc65199a35.jpg), and [temperature](https://cloud.githubusercontent.com/assets/24979274/22472193/80ba1a7c-e79a-11e6-82f3-2b2cc2285512.jpg) data easily availible.

<p align="left"> 
  <img src="https://cloud.githubusercontent.com/assets/24979274/22262470/9b3d7c54-e236-11e6-800c-9a5fee420b1d.png"> 
</p>


Installation
------------
Install the latest version of [Raspbian](https://www.raspberrypi.org/downloads/raspbian/) onto the Pi.

Install the Enviro pHat library onto the Pi by typing the following:
```
curl -sS get.pimoroni.com/envirophat | bash
``` 
Type `y` when prompted, then restart the Pi to ensure the changes occur.


To install this repository, type:
```
git clone https://github.com/markdgoodrich/GardenBox.git
```

You are now ready to start recording data.



Collecting Data
---------------
To constantly record & transmit data, type:
```
cd GardenBox
python GardenBox.py
```
You will be prompted asking for your computer's User name, IP address, and the desired file directory for the exported data files.
Hit `Enter` after each prompt.
```
Type in the User name for your computer (the one you'll be sending the data files to): 
Type in the IP address of your computer (example: 192.168.0.100): 
Type the directory and folder path where you'd like the data to transfer to (example: ~/Documents/LemonTreePi/Data_Text): 
```
You will see this message:
```
#insert nohup message out to nohup.out
```
You can now `exit` from your Pi; the monitoring process will continue without halting.
