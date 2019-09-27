import os
import sys
from argparse import ArgumentParser

from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)

### แก้เป็น *
from linebot.models import *

app = Flask(__name__)

###แก้ โทเคน
# get channel_secret and channel_access_token from your environment variable
channel_secret = '8b1c3517ec7905aaa49edca2805c4d02'
channel_access_token = '7am3KDdBRsl/TiNrPKEhb/43c4RQyaLV52hrxfmeHxQiGyBkOrObnDh9HGbLYcFEG4GAun7sbA6ksB8ncDqfnwu83CfxmfFjRPSb4GX7tbgbOZG/jaubZ5FyCnE407o+bR4LFtt1hlBcjK0CDwVP+gdB04t89/1O/w1cDnyilFU='

line_bot_api = LineBotApi(channel_access_token) ##ตัวส่งapi
handler = WebhookHandler(channel_secret)

#### แก้ route
@app.route("/webhook", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def message_text(event):

    ### function reply_token
    Reply_token = event.reply_token #### reply token
    text_fromUser = event.message.text ### ข้อความจาก ยูสเซอ
    print(text_fromUser)

    #### ตรวจสอบ ว่า ภายในข้อความของยูส มีคำว่า เช็คราคา อยู่หรือไม่ ถ้าใช้ บอทจะตอบกลับเป็น flex message
    if 'เช็คราคา' in text_fromUser:
        from Resource.bxAPI import GetBxPrice
        from random import randint
        num = randint(1,10)
        data = GetBxPrice(Number_to_get=num) ## เก็บจำนวนข้อมูล

        from Resource.FlexMessage import setbubble , setCarousel

        flex = setCarousel(data)

        from Resource.reply import SetMenuMessage_Object , send_flex

        flex = SetMenuMessage_Object(flex)
        send_flex(Reply_token,file_data = flex,bot_access_key = channel_access_token)

    ##### check newsapi
    elif 'เช็คข่าวสาร' in text_fromUser:
        text = TextSendMessage(text='ท่านได้ทำการเลือกเมนู เช็คข่าวสาร') #setup text message
        
        from Resource.FlexMessage import news_setbubble 
        from Resource.reply import SetMenuMessage_Object , send_flex
        from Resource.newsAPI import get_cnn_news

        data = get_cnn_news()
        flex = news_setbubble(data['title'],data['description'],data['url'],data['image_url'])
        
        text = TextSendMessage(text='รายงานข่าวสารสำหรับ CNN ล่าสุด').as_json_dict()

        msg = SetMenuMessage_Object([text,flex])

        send_flex(Reply_token,file_data = msg,bot_access_key = channel_access_token)
        

    else:
        text_list = [
            'ฉันไม่เข้าใจที่คุณพูดค่ะ กรุณาลองใหม่อีกครั้งนะค่ะ',
            'ขออภัยค่ะ ฉันไม่เข้าใจจริงๆค่ะ ลองใหม่นะค่ะ',
            'ขอโทษต่ะ ไม่ทราบว่า มีความหมายอย่างไรค่ะ',
            'กรุณาลองพิมใหม่ได้ไหมค่ะ'
        ]

        from random import choice

        text_data = choice(text_list)

        text = TextSendMessage(text=text_data)

        line_bot_api.reply_message(Reply_token,text)


@handler.add(FollowEvent)
def RegisRichmenu(event):
    userid = event.source.user_id
    disname = line_bot_api.get_profile(user_id=userid).display_name
    ### setup quick reply button
    button_1 = QuickReplyButton(action=MessageAction(label='เช็คราคา',text='เช็คราคา'))
    button_2 = QuickReplyButton(action=MessageAction(label='เช็คข่าวสาร',text='เช็คข่าวสาร'))
    qbtn = QuickReply(items=[button_1,button_2])
    ### text message object
    text = TextSendMessage(text='สวัสดีคุณ  {}  ยินดีต้อนรับสู่บริการแชทบอท'.format(disname))
    text_2 = TextSendMessage(text='กรุณาเลือกเมนูที่ท่านต้องการ',quick_reply = qbtn)
    ### link richmenu
    line_bot_api.link_rich_menu_to_user(userid,'richmenu-3139e071b8f186e8f616e94d320bfca7')
    ### reply message when user follow
    line_bot_api.reply_message(event.reply_token,messages=[text,text_2])







if __name__ == "__main__":
    app.run(port=200)
    #heroku cloud server https://uncletut01.herokuapp.com//webhook




