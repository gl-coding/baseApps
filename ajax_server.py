#encoding=utf8
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options
import json

define("port", default=8000, help="run on the given port", type=int)

#just for ajax，实现跨域请求Server
class BaseHandler(tornado.web.RequestHandler):

    #blog.csdn.net/moshowgame 解决跨域问题
    def set_default_headers(self):
        print("setting headers!!!")
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Headers', '*')
        self.set_header('Access-Control-Max-Age', 1000)
        #self.set_header('Content-type', 'application/json')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.set_header('Access-Control-Allow-Headers',#'*')
                        'authorization, Authorization, Content-Type, Access-Control-Allow-Origin, Access-Control-Allow-Headers, X-Requested-By, Access-Control-Allow-Methods')


    def post(self):
        self.write('some post')

    def get(self):
        self.write('some get')

    def options(self):
        # no body
        self.set_status(204)
        self.finish()

class IndexHandler(BaseHandler):
    def get(self):
        greeting = self.get_argument("message")
        self.write(greeting + ", friendly user!")

    def post(self):
        res = self.request.body
        print res
        print type(res)
        self.write(res)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

