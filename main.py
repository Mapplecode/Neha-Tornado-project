import os.path
import tornado.escape
import tornado.ioloop
import tornado.web
import motor.motor_tornado
from view import MainHandler,login_handler,register_handler,get_registeration
from db_connect import Mydb




def make_app():
    settings = {
        "template_path": os.path.join(os.path.dirname(__file__), "templates"),
        "static_path": os.path.join(os.path.dirname(__file__), "static"),
        'db':motor.motor_tornado.MotorClient().tornado

    }
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/login", login_handler),
        (r"/register", register_handler),
        (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": os.path.dirname(os.path.realpath(__file__)) + "/static"}),
        (r"/get_registeration", get_registeration),
    ],
        settings=settings
    )

if __name__ == "__main__":
    app = make_app()
    app.autoreload=True
    app.listen(5000)
    tornado.ioloop.IOLoop.current().start()


