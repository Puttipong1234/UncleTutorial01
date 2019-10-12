from threading import Thread
import time
import requests
from bxAPI import GetBxPrice
import time
from flask import Flask

app = Flask(__name__)


class NewThread(Thread):

    def __init__(self,name, delay,user):
        Thread.__init__(self)
        self.delay = delay
        self.name = name
        self.stop = False
        self.user = user

    def run(self):
        while 1:
            time.sleep(self.delay)
            print([self.name + ' sending message to {}'.format(i) for i in self.user])
            # res = GetBxPrice()
            # print(res)
            if self.stop: 
                print('stop sending message')
                break
    
    def stoprun(self):
        self.stop = True

thread01 = ''
uid = []

@app.route('/start')
def start():
    global thread01
    global uid
    thread01 = NewThread('Thread1',1,uid)
    thread01.start()
    return 'u start notify {}'.format(uid)

@app.route('/stop')
def stop():
    global thread01
    global uid
    thread01.stoprun()
    return 'u start notify {}'.format(uid)

@app.route('/add/<id>')
def add(id):
    global uid
    uid.append(id)
    return '<h1>u add new user {}</h1>'.format(id)



if __name__ == '__main__':
    app.run(port=200)
    


