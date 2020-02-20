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

batt_lvl = 99
dist_covered = 100
speed_val = 50
robot_state = "moving"
# bot_oled = oled_display.Oled_display(robot_state, str(speed_val), batt_lvl, dist_covered)

bot = tracker.Tracker(14, 12, 13, 32, 26, 27, 23)
robot_state = "Stop"
blade_state = "Off"
bot.setup()
bot.setSpeed(70)

html = open("index.new.html", "r")
html = html.read()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    request = str(request)
    myRequest = request
    print('Content = %s' % request)
    robot_command_request = request.find('/?robot_command=')
    robot_direction_request = request.find('/?robot_direction=')
    robot_speed_request = request.find('/?robot_speed=')
    blade_toggle = request.find('/?robot=blade_toggle')
    isControlKey = False
    if robot_direction_request > 0:

        robot_command = myRequest.split("$")

        a1 = int(robotCommand[1])
        b1 = int(robotCommand[2])
        a2 = int(robotCommand[3])
        b2 = int(robotCommand[4])

        bot.manualSetDir(a1, b1, a2, b2)
        isControlKey = True

    if robot_speed_request > 0:

        robot_command = myRequest.split("$")

        en1 = int(robotCommand[1])
        en2 = int(robotCommand[2])

        bot.manualSetSpeed(en1, en2)
        isControlKey = True

    if robot_command_request > 0:

        robotCommand = myRequest.split("$")

        en1 = int(robotCommand[1])
        a1 = int(robotCommand[2])
        b1 = int(robotCommand[3])

        en2 = int(robotCommand[4])
        a2 = int(robotCommand[5])
        b2 = int(robotCommand[6])

        bot.manualSetAll(en1, a1, b1, en2, a2, b2)
        isControlKey = True

    if blade_toggle == 6:
        print('toggling blade')
        blade_state = bot.blade_toggle(blade_state)
        isControlKey = True

    bot_oled.display(robot_state, str(speed_val), batt_lvl, dist_covered)

    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    if(not isControlKey):
        conn.send(html)
    else:
        conn.send("Hi there")
    conn.sendall('\n')
    conn.close()
