import json
import requests


def ReplyMessage(Reply_token, TextMessage, Line_Access_Token):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'

    Authorization = 'Bearer {}'.format(Line_Access_Token) ##à¸—à¸µà¹ˆà¸¢à¸²à¸§à¹†
    print(Authorization)
    
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization':Authorization
    }

    data = {
        "replyToken":Reply_token,
        "messages":[{
            "type":"text",
            "text":TextMessage
        },{
            "type":"text",
            "text":'ท่านสามารถใช้งานโดยการพิมพ์ประโยคที่ต้องการค้นหาค่ะ'
        }]
    }
    ##before
    print(type(data))
    
    data = json.dumps(data) ## dump dict >> Json Object
    ##after
    print(type(data))

    r = requests.post(LINE_API, headers=headers, data=data) 
    return 'OK'


def PushMessage(userid, TextMessage, Line_Access_Token):
    LINE_API = 'https://api.line.me/v2/bot/message/push'

    Authorization = 'Bearer {}'.format(Line_Access_Token) ##à¸—à¸µà¹ˆà¸¢à¸²à¸§à¹†
    print(Authorization)
    
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization':Authorization
    }

    data = {
        "to": userid,
        "messages":[
            {
                "type":"text",
                "text":TextMessage
            },
            {
                "type":"text",
                "text":"Hello, world2"
            }
        ]
    }
    ##before
    print(type(data))
    
    data = json.dumps(data) ## dump dict >> Json Object
    ##after
    print(type(data))

    r = requests.post(LINE_API, headers=headers, data=data)
    print(r) 
    return 'OK'




def SetMenuMessage_Object(Message_data,Quick_Reply = None):
    file_data = {"replyToken":'', "messages": []}

    if type(Message_data) is list:
        for message in Message_data:
            file_data['messages'].append(message)

    else :
        file_data['messages'].append(Message_data)
        
    return file_data

def send_flex(reply_token,file_data,bot_access_key):
    
    LINE_API = 'https://api.line.me/v2/bot/message/reply'

    Authorization = 'Bearer {}'.format(bot_access_key)

    headers = {'Content-Type': 'application/json; charset=UTF-8',
  'Authorization': Authorization}

    file_data['replyToken'] = reply_token
    #### dumps file จาก dict ให้เป็น json
    file_data = json.dumps(file_data)
    r = requests.post(LINE_API, headers=headers, data=file_data) # ส่งข้อมูล

    return r

    

