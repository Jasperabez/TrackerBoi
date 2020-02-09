from machine import Pin, I2C
#oled library
import ssd1306
status = 0
batt_lvl=99
dist_covered=100
# ESP32 Pin assignment 
i2c = I2C(-1, scl=Pin(22), sda=Pin(21))
oled_width = 128
oled_height = 32
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
oled.text('Welcome!', 0, 0)
oled.text('Press ON,', 0, 10)
oled.text('To start!', 0, 20)
oled.show()

def web_page():

  if status == 1:
    state="ON"
  else:
    state="OFF"
  
  html = """<html><head> <title>TrackerBoi</title> <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" href="data:,"> <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
  h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #e7bd3b; border: none; 
  border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
  .button2{background-color: #4286f4;}</style></head><body> <h1>TrackerBoi</h1> 
  <p>Pressed: """ + state + """</p>  
  <p>Battery Level: """ + str(batt_lvl) + """</p>
  <p>Distance Travelled: """ + str(dist_covered) + """ metres</p>
  <p>Controls: <br> <a href="/?trackerboi=on"><button class="button">ON</button></a><br></p>
  <p><a href="/?trackerboi=off"><button class="button button2">OFF</button></a></p></body></html>"""
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
  trackerboi_on = request.find('/?trackerboi=on')
  trackerboi_off = request.find('/?trackerboi=off')
  if trackerboi_on == 6:
    status = 1
    oled.fill(0)
    oled.text('TrackerBoi: ON', 0, 0)
    oled.text('Batt Lvl:%d' % (batt_lvl), 0, 10)
    oled.text('Distance:%d m' % (dist_covered), 0, 20)
    oled.show
  if trackerboi_off == 6:
    status = 0
    oled.fill(0)
    oled.text('TrackerBoi: OFF', 0, 0)
    oled.text('Batt Lvl:%d' % (batt_lvl), 0, 10)
    oled.text('Distance:%d m' % (dist_covered), 0, 20)
    oled.show
  response = web_page()
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
  conn.close()
  oled.show()