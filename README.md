# graduation-project
Intelligent Traffic Lights System for Emergency Vehicles Design

## BeagleBone Black Instructions:

### For network sharing through Laptop: 

http://lanceme.blogspot.com.eg/2013/06/windows-7-internet-sharing-for.html

### For using the Laptop as a display:

1- install putty on the Laptop to open BeagleBone terminal through ssh: http://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html
2- install tightvnc on the Laptop: http://www.tightvnc.com/download.php
3- open ssh connection using putty through the ip address: 192.168.7.2 username: root
4- on the beaglebone type tightvnc in the terminal and enter a new password if its the first time to use it (the current tightvnc password is eslamsamir)
5- run the following command on the BeagleBone terminal tightvncserver :1 geometry 1920x1080 -depth 24 -dpi 96
6- open tightvnc on the laptop and connect to the ip address 192.168.7.2:1 and enter the password you entered in the BeagleBone terminal (eslamsamir)
7- tightvnc is now displaying the linux over the BeagleBone

### solution for chromium can't run as root problem if it happened:

http://www.canbike.org/information-technology/precise-puppy-5-4-3-chromium-browser-run-as-root-and-start-maximized.html
