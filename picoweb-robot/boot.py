from machine import Pin

robot_state = "Stop"

import esp
esp.osdebug(None)

import gc
gc.collect()

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

def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('Test', 'Test1234')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
