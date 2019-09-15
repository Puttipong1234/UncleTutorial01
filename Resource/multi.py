from flask import Flask
import threading
import time
import requests
from bxAPI import GetBxPrice


app = Flask(__name__)

#### function ที่ต้องให้การรัน ไปเรื่อยๆ
def getprice(enable = True):
    t = threading.currentThread()
    while getattr(t, "do_run", True):
        try:
            res = GetBxPrice()
            print(res)
        except:
            print('no internet connection')
        time.sleep(3)
#### enable route to start requesting
@app.route('/start')
def start():
    t.start()

    return 'hello'
### enable route to stop requesting
@app.route('/stop')
def stop():
    t.do_run = False
    return 'OK'

if __name__ == '__main__':
    t = threading.Thread(target=getprice, args=("task",))

    app.run(debug=True)