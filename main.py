import os.path
import tornado.escape
import tornado.ioloop
import tornado.web
from view import MainHandler,login_handler,\
    register_handler,get_registeration,logout_handler,user_info_handeler

secret_key  = 'cXdlcXdkd2RmcXdlZmVmZg=='
def make_app():
    settings = {
        "template_path": os.path.join(os.path.dirname(__file__), "templates"),
        "static_path": os.path.join(os.path.dirname(__file__), "static"),

    }
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/login", login_handler),
        (r"/logout_user", logout_handler),
        (r"/register", register_handler),
        (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": os.path.dirname(os.path.realpath(__file__)) + "/static"}),
        (r"/get_registeration", get_registeration),
        (r"/user_info", user_info_handeler),
    ],
        settings=settings, cookie_secret=f"__TODO:{secret_key}"
    )

if __name__ == "__main__":
    app = make_app()
    app.autoreload=True
    app.listen(5000)
    tornado.ioloop.IOLoop.current().start()


