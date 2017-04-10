import tornado.ioloop
import tornado.web

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

app = tornado.web.Application([
    (r"/", MainApp),
    ])

app.listen(8888)
tornado.ioloop.IOLoop.instance().start()
