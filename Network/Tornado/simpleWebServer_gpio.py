import tornado.ioloop
import tornado.web
import tornado.websocket
import RPi.GPIO as GPIO

led = 13

#Initialize
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

html_text = '''
<!DOCTYPE html>
<html>
 <body>
  <h2>LED 13 Switch ON/OFF</h2>
   <input type='button' id='led_on' value='ON'>
   <input type='button' id='led_off' value='OFF'>
   <script src="//192.168.3.4/jquery.min.js"></script>
   <script src="//192.168.3.4/ws.js"></script>
   <hr>
   WebSocket Status:
   <br>
   <div id="ws-status">Waiting...</div>
 </body>
</html>
'''

class MainApp (tornado.web.RequestHandler):
    def get(self):
        self.write(html_text)

class WSHandler (tornado.websocket.WebSocketHandler):
    def on_message(self, message):
        if message == "on_13":
            GPIO.output(led, True)
            print("LED is on")
        if message == "off_13":
            GPIO.output(led, False)
            print("LED is off")

app = tornado.web.Application([
    (r"/", MainApp),
    (r'/ws', WSHandler),
    ])

app.listen(8888)
tornado.ioloop.IOLoop.instance().start()
