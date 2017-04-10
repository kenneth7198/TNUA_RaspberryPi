import tornado.ioloop
import tornado.web

class MainApp (tornado.web.RequestHandler):
    def get(self):
        self.write("Hello Tornado!")

app = tornado.web.Application([
    (r"/", MainApp),
    ])

app.listen(8888)
tornado.ioloop.IOLoop.instance().start()
