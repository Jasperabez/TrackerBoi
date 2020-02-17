import gc
import esp
import time
import tracker
import oled_display

do_ap()

try:
    import usocket as socket
except:
    import socket

esp.osdebug(None)

gc.collect()

batt_lvl=99
dist_covered=100
speed_val = 50
bot_oled = oled_display.Oled_display(robot_state,str(speed_val),batt_lvl,dist_covered);

bot = tracker.Tracker(14, 12, 13, 32, 26, 27, 23)
robot_state = "Stop"
blade_state = "Off"
bot.setup()
bot.setSpeed(70)

html = open("index.html","r")
html = html.read()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    request = str(request)
    print('Content = %s' % request)
    request_iframe = request.find('/iframe')
    robot_stop = request.find('/?robot=stop')
    robot_forward = request.find('/?robot=forward')
    robot_backward = request.find('/?robot=backward')
    robot_right = request.find('/?robot=right')
    robot_left = request.find('/?robot=left')
    speed_change = request.find('/?speed=')
    blade_toggle = request.find('/?robot=blade_toggle')
    isControlKey = False
    if speed_change == 6:
        try:
            speed = int(request[14:17])
        except:
            speed = int(request[14:16])
        print(speed)
        bot.setSpeed(speed)
    if robot_stop == 6:
        print('robot stopping...')
        robot_state = "Stop"
        bot.stop()
        isControlKey = True
    if robot_forward == 6:
        print('robot advancing forward...')
        robot_state = "Forward"
        bot.forward()
        isControlKey = True
    if robot_backward == 6:
        print('robot retreating backward...')
        robot_state = "Backward"
        bot.backward()
        isControlKey = True
    if robot_right == 6:
        print('robot turning right...')
        robot_state = "Right"
        bot.right()
        isControlKey = True
    if robot_left == 6:
        print('robot turning left...')
        robot_state = "Left"
        bot.left()
        isControlKey = True
    if blade_toggle == 6:
        print('toggling blade')
        blade_state = bot.blade_toggle(blade_state)
        isControlKey = True
    bot_oled.display(robot_state,str(speed_val),batt_lvl,dist_covered)
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    if(not isControlKey):
        conn.send(html)
    else:
        conn.send("Hi there")
    conn.sendall('\n')
    conn.close()
