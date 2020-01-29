do_ap()

try:
  import usocket as socket
except:
  import socket

import tracker
import esp
esp.osdebug(None)

import gc
gc.collect()

bot = tracker.Tracker(14,12,13,25,26,27)
robot_state = "Stop"
bot.setup()

def web_page():
  
  html = """
    <html>
        <head> 
            <title>ESP Web Server</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link rel="icon" href="data:,"> 
            <script>
              function submitSpeed(){
                var form = document.getElementById("speedEntry");
                speed = document.getElementById("speedValue").value;
                speed = parseInt(speed,10)
                if(Number.isInteger(speed) && speed>=0 && speed<=100){
                  form.submit();
                }
                else{
                  window.alert("Not valid case, need to be between 0 and 100")
                }
              }
            </script>
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
                <form id="speedEntry" action="./">
                  <input type="text" id="speedValue" name="speed"><br><br>
                  <input type="button" onclick="submitSpeed()" value="Submit">
                </form>
                <script>
                  document.getElementById('speedValue').addEventListener('keypress', function(event) {
                  if (event.keyCode == 13) {
                      event.preventDefault();
                      submitSpeed();
                  }
                  })
                </script>
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
  speed_change = request.find('/?speed=')
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
  if robot_forward == 6:
    print('robot advancing forward...')
    robot_state = "Forward"
    bot.forward()
  if robot_backward == 6:
    print('robot retreating backward...')
    robot_state = "Backward"
    bot.backward()
  if robot_right == 6:
    print('robot turning right...')
    robot_state = "Right"
    bot.right()
  if robot_left == 6:
    print('robot turning left...')
    robot_state = "Left"
    bot.left()
  response = web_page()
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
  conn.close()