---
layout: post
title: Simple Webserver On ESP32 Micropython
---

Don't you want to remote control your esp32 robot? read this guide then :)

# Network

Can either choose to connect to a common access point(AP) or use the ESP32 itself as an AP

## Common AP

Put the code below into your boot.py

```python
def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('<essid>', '<password>')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
```

## ESP32 as AP

Put the code below into your boot.py and PLEASE note authmode have to be set to 3 else your AP is unencrpyted

```python
def do_ap():
    import network
    ssid = 'IAM_AP'
    password = 'IAMPassword'
    authmode = 3  # WPA2
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid=ssid, password=password, authmode=authmode)
    while ap.active() == False:
      pass
    print('Connection successful')
    print(ap.ifconfig())
```

You can include both if your boot.py and just call the function accordingly depending on your needs

# Webserver

The following code is largely taken from [random nerd tutorials](https://randomnerdtutorials.com/esp32-esp8266-micropython-web-server/) with some modifications. I'm using do_connect over here but you can choose to use do_ap if you wish. Copy and dump the code in your main.py.

```python
do_connect()

try:
  import usocket as socket
except:
  import socket

import esp
esp.osdebug(None)

import gc
gc.collect()

robot_state = "Stop"

def web_page():
  
  html = """
    <html>
        <head> 
            <title>ESP Web Server</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link rel="icon" href="data:,"> 
            <style>
                html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
                h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}
                .button{display: inline-block; background-color: #e7bd3b; border: none; border-radius: 4px; color: white;  padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
                .buttonStop{background-color: red;}
            </style>
        </head>
        <body> 
            <h1>ESP Web Server</h1> 
                <p>Robot state: <strong>""" + robot_state + """</strong></p>
                <p><a href="/?robot=stop"><button class="button buttonStop">STOP</button></a></p>
                <p><a href="/?robot=forward"><button class="button">FORWARD</button></a></p>
                <p><a href="/?robot=backward"><button class="button">BACKWARD</button></a></p>
                <p><a href="/?robot=right"><button class="button">RIGHT</button></a></p>
                <p><a href="/?robot=left"><button class="button">LEFT</button></a></p>
        </body>
    </html>
    """
  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  request = str(request)
  print('Content = %s' % request)
  robot_stop = request.find('/?robot=stop')
  robot_forward = request.find('/?robot=forward')
  robot_backward = request.find('/?robot=backward')
  robot_right = request.find('/?robot=right')
  robot_left = request.find('/?robot=left')
  if robot_stop == 6:
    print('robot stopping...')
    robot_state = "Stop"
  if robot_forward == 6:
    print('robot advancing forward...')
    robot_state = "Forward"
  if robot_backward == 6:
    print('robot retreating backward...')
    robot_state = "Backward"
  if robot_right == 6:
    print('robot turning right...')
    robot_state = "Right"
  if robot_left == 6:
    print('robot turning left...')
    robot_state = "Left"
  response = web_page()
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
  conn.close()
```


The code should be pretty straight forward, but the reason why all the robot states == 6 is because when you use find for the specific href on the original http request it would give you the index at 6 always. That is if it exist, on the other hand if it doesn't it returns 0. 

If you want the code to interact with real electronics, just replace the print statement "robot ......" to code that interacts with the pins

# Conclusion

that's pretty much it, I'll soon make a guide that showcase how to host a webserver on your ESP32 using a flask, django like library called picoweb
