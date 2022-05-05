import tornado.ioloop
import tornado.web
import os,codecs
import json
import tornado.auth
import tornado.escape
import pymongo
from db_connect import mycol
from enc_dec import encrypt_message
request_handeler = tornado.web.RequestHandler

def add_user(user):
    mydict = user
    dec_pass = encrypt_message(mydict['password'])
    mydict['password'] = dec_pass
    x = mycol.insert_one(mydict)
    return 'Done'

def find_user(email):
    user_list = list()

    for users in mycol.find({ "email": email}):
        # print(users)
        user_list.append(users)
    return user_list


def html_reader(html):
    template_path = os.path.join(os.getcwd() ,'template' ,html)
    f = codecs.open(template_path, 'r').read()
    return str(f)

class BaseHandler(request_handeler):
    def get_current_user(self):
        return self.get_secure_cookie("user")

class MainHandler(request_handeler):
    def get(self):
        if not self.get_secure_cookie("user"):
            self.redirect("/login")
            return
        self.render('template/index.html')

class login_handler(request_handeler):
    def get(self):
        self.render('template/login.html')

    def post(self):
        dic_data = tornado.escape.json_decode(self.request.body)
        existing_users = find_user(dic_data['email'])
        if existing_users:
            existing_user = existing_users[0]
            print(existing_user)
            self.set_secure_cookie("user",str(existing_user['full_name']).encode())
            self.set_secure_cookie("email",str( existing_user['email']).encode())
            response =   {'success': True, 'message': 'User added successfully'}
            self.write(json.dumps(response))

class logout_handler(request_handeler):
    def get(self):
        self.clear_cookie("user")
        self.clear_cookie("email")
        self.clear_cookie("disabilities")
        self.render("template/login.html")

class register_handler(request_handeler):
    def get(self):
        self.render('template/register.html')

class user_info_handeler(request_handeler):
    def get(self):
        user = find_user(self.get_secure_cookie("email").decode())
        print(user)
        self.render('template/user_info.html',user=user[0])

class get_registeration(request_handeler):
    def post(self, *args):
        dic_data = tornado.escape.json_decode(self.request.body)
        # useful code goes here
        response = dict()
        try:
            existing_users = find_user(dic_data['email'])
            if len(existing_users) > 0 :
                response =  {'success':False,'message':'User with same email already exists'}
            else:
                add_user(dic_data)
                response =   {'success': True, 'message': 'User added successfully'}
        except Exception as e:
            print(e)
            response = {'success':False,'message':str(e)}
        self.write(json.dumps(response))
