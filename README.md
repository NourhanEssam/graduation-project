# graduation-project
Intelligent Traffic Lights System for Emergency Vehicles Design

## BeagleBone Black Instructions:

### Getting Started:

1- Connect the BeagleBone to the Laptop using the usb cable

2- Open the start.htm file and follow the instructions

3- If you are having a problem installing the drivers follow these instructions and then try installing it again:
https://www.element14.com/community/community/designcenter/single-board-computers/next-gen_beaglebone/blog/2016/11/14/beagle-bone-black-window-10-driver-fix

4- Never disconnect the BeagleBone from the power source without shutting it down first. You have to use the shutdown command or use the power button.

### For network sharing through Laptop: 

connect the BeagleBone with the Laptop though an ethernet cable and follow these instructions:
http://lanceme.blogspot.com.eg/2013/06/windows-7-internet-sharing-for.html

### For using the Laptop as a display:

1- install putty on the Laptop to open BeagleBone terminal through ssh:
http://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html

2- install tightvnc on the Laptop: http://www.tightvnc.com/download.php

3- open ssh connection using putty through the ip address: 192.168.7.2 username: root

4- on the beaglebone type tightvnc in the terminal and enter a new password if its the first time to use it (the current tightvnc password is eslamsamir)

5- run the following commands on the BeagleBone terminal: 

tightvncserver

tightvncserver :1 geometry 1920x1080 -depth 24 -dpi 96

6- open tightvnc on the laptop and connect to the ip address 192.168.7.2:1 and enter the password you entered in the BeagleBone terminal (eslamsamir)

7- tightvnc is now displaying the linux over the BeagleBone

### solution for chromium can't run as root problem if it happened:

http://www.canbike.org/information-technology/precise-puppy-5-4-3-chromium-browser-run-as-root-and-start-maximized.html


## Raspberry Pi Instructions:

### Touchscreen Guide

https://www.element14.com/community/docs/DOC-78156/l/raspberry-pi-7-touchscreen-display

### Raspberry Pi remote control from Laptop:

https://www.raspberrypi.org/documentation/remote-access/vnc/

### Virtual Keyboard for the Touchscreen:

sudo apt-get update
sudo apt-get upgrade
sudo apt-get install at-spi2-core
sudo apt-get install florence
