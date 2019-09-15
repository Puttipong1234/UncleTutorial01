import pprint
from flask import Flask , request
## from{ name of your file } import search
# from wolf import search_wiki
## การเข้าผ่าน ไฟล์ทั่วไป from folder.filename import function
from Resource.wolf import search_wiki


app = Flask(__name__)
#access token ของบอทท่าน
access_token ='7am3KDdBRsl/TiNrPKEhb/43c4RQyaLV52hrxfmeHxQiGyBkOrObnDh9HGbLYcFEG4GAun7sbA6ksB8ncDqfnwu83CfxmfFjRPSb4GX7tbgbOZG/jaubZ5FyCnE407o+bR4LFtt1hlBcjK0CDwVP+gdB04t89/1O/w1cDnyilFU='




@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/webhook', methods=['POST','GET'])
def webhook():
    if request.method == 'POST':

        pp = pprint.PrettyPrinter(indent=3)
        ### dictionary from line
        data = request.json
        print(data)
        data_show = pp.pprint(data)

        ## extract text from line
        text_fromline = data['events'][0]['message']['text']
        ## ค้นหาคำจาก wikipedia
        result = search_wiki(text_fromline)

        ### import function ในการส่งmessage reply.py
        from reply import ReplyMessage

        ReplyMessage(Reply_token=data['events'][0]['replyToken'],
        TextMessage=result,
        Line_Access_Token= access_token ## insert access token
        )

        return 'OK'

    elif request.method == 'GET':
        return 'นี้คือลิงค์เว็บสำหรับรับ package'

if __name__ == "__main__":
    app.run(port=200)





