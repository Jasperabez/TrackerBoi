---
layout: post
title: Picoweb Webserver ESP32 Micropython
---

I always wanted to learn flask or django so I decided to recode the Simple Webserver with Picoweb, a library that's extremely similar to the 2 library I mentioned but for micropython.

# DIY or clone repo

You can either to choose to clone the repo with all the micropython modules loaded, or you can choose to challenge yourself and build it by yourself. 

## Clone repo

If you want choose to clone it, here's the [link](https://github.com/Jasperabez/TrackerBoi/tree/master/picoweb-robot), and follow the instructions below.

- clone the repo (git clone)
- transfer all files and directories into your ESP32 (ampy, thonny)
- press reset button
- connect to the AP using credentials found in boot.py OR connect to common AP by modifying value in boot.py (change to do_connect if so)
- navigate to the IP address as displayed on the terminal

## DIY

If you are feeling adventureous and smart these are the steps:

- connect your ESP32 to the internet 
- type the following commands in repl
    - `import upip`
    - `upip.install('picoweb')`
- remove the folder "uasyncio" from the folder lib (weird bug, picoweb didn't install correct stuff)
- install another version of uasyncio using command `upip.install('uasyncio')`
- run more commands
    - `upip.install('pycopy-ulogging')`
    - `upip.install('utemplate')`
- IMPORTANT step, open up ./lib/picoweb/_init_.py, search for awritestr.. at line 253 and change that to awrite..
- copy main.py and boot.py from the [repo](https://github.com/Jasperabez/TrackerBoi/tree/master/picoweb-robot) I mentioned earlier
- that's all and since you're a pro you know what to do (hint: follow the bottom half of Clone Repo instructions)


# Performance

By the time after you run it you should realize that picoweb is kinda of slower that the simple webserver, and you're right I feel that too. That's probably because of the extra overhead code that it has, and would probably not be suited for the use case of controlling a robot. However, it is definitely a valid choice for more sophisacated web apps that you want to host on your esp32.

