import tornado.ioloop
import tornado.web

class GetHandler(tornado.web.RequestHandler):
    def get(self):
        res = self.get_argument("args")
        self.write("hello, " + res)

class PostHandler(tornado.web.RequestHandler):
    #process for post json
    def post(self):
        res = self.request.body
        print res
        self.write(res)

application = tornado.web.Application([
    (r"/", PostHandler),
    (r"/test", GetHandler),
    ])

if __name__ == '__main__':
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
