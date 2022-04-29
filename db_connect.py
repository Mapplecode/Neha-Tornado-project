import motor.motor_tornado
client = motor.motor_tornado.MotorClient('localhost', 27017)
Mydb = client.db_test
