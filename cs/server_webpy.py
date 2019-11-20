#encoding=utf8
import web

urls = (
     '/', 'hello'
)
app = web.application(urls, globals())

class hello:
    def GET(self):
        info = web.input().info
        return info

    def POST(self):
        info = web.data()
        print type(info)
        return info

if __name__ == "__main__":
    app.run()
