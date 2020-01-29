def do_ap():
    import network
    ssid = 'Jabez_AP'
    password = 'hihi1234'
    authmode = 3  # WPA2
    ap = network.WLAN(network.AP_IF)
    ap.ifconfig(('192.168.15.1', '255.255.255.0', '192.168.15.1', '8.8.8.8'))
    ap.active(True)
    ap.config(essid=ssid, password=password, authmode=authmode)
    while ap.active() == False:
      pass
    print('Connection successful')
    print(ap.ifconfig())