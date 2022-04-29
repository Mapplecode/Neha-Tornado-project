import tornado.ioloop
import tornado.web
import os,codecs
import json
import tornado.auth
import tornado.escape
from db_connect import Mydb
import asyncio
import pprint
from tornado.ioloop import IOLoop
from bson.objectid import ObjectId
from motor.motor_tornado import MotorCollection


def add_user(user):
    Mydb.test_collection.insert_one(user)
    return 'Done'
def find_user(email):
    result = Mydb.testcollection.find({'email': email}).count() > 0
    print(result)
    if result != 0:
        print('exists')
        print(dir(result))
        print(result.result())
    return


def html_reader(html):
    template_path = os.path.join(os.getcwd() ,'template' ,html)
    f = codecs.open(template_path, 'r').read()
    return str(f)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class login_handler(tornado.web.RequestHandler):
    def get(self):
        self.write(html_reader('login.html'))

class register_handler(tornado.web.RequestHandler):
    def get(self):
        self.write(html_reader('register.html'))

class get_registeration(tornado.web.RequestHandler):
    def post(self, *args):
        dic_data = tornado.escape.json_decode(self.request.body)
        # useful code goes here
        try:
            async def do_find_one():
                document = await Mydb.test_collection.find({'email':dic_data['email'] })
                pprint.pprint(document)

            IOLoop.current().run_sync(do_find_one)
        except Exception as e:
            print(e)
        # add_user(dic_data)
        self.write(json.dumps({'status': 'ok', 'sent': 1}))
