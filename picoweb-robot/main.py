do_ap()

#
# This is an example of a (sub)application, which can be made a part of
# bigger site using "app mount" feature, see example_app_router.py.
#
import picoweb

def printDirect(direct):
    directions = {
    "stop":"robot stopping...",
    "forward":"robot advancing forward...",
    "backward":'robot retreating backward...',
    "right":'robot turning right...',
    "left":'robot turning left...'
    }
    print(directions.get(direct, "robot stopping"))

app = picoweb.WebApp(__name__)
 
@app.route("/")
@app.route("/robot=stop")
def index(req, resp):
    printDirect(req.path[7:])
    yield from picoweb.start_response(resp)
    yield from app.render_template(resp, "buttons.tpl", (req,))
    
@app.route("/robot=forward")
def forward(req, resp):
    printDirect(req.path[7:])
    yield from picoweb.start_response(resp)
    yield from app.render_template(resp, "buttons.tpl", (req,))
    
@app.route("/robot=backward")
def backward(req, resp):
    printDirect(req.path[7:])
    yield from picoweb.start_response(resp)
    yield from app.render_template(resp, "buttons.tpl", (req,))
    
@app.route("/robot=right")
def right(req, resp):
    printDirect(req.path[7:])
    yield from picoweb.start_response(resp)
    yield from app.render_template(resp, "buttons.tpl", (req,))
    
@app.route("/robot=left")
def left(req, resp):
    printDirect(req.path[7:])
    yield from picoweb.start_response(resp)
    yield from app.render_template(resp, "buttons.tpl", (req,))
 
app.run(debug=True, host = "192.168.4.1", port=80)


