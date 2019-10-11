import os
import sys
from argparse import ArgumentParser

from flask import Flask, request, abort , send_from_directory , render_template
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)

### แก้เป็น *
from linebot.models import *

from Resource.reply import SetMenuMessage_Object , send_flex

app = Flask(__name__)

###แก้ โทเคน
# get channel_secret and channel_access_token from your environment variable
channel_secret = '8b1c3517ec7905aaa49edca2805c4d02'
channel_access_token = '7am3KDdBRsl/TiNrPKEhb/43c4RQyaLV52hrxfmeHxQiGyBkOrObnDh9HGbLYcFEG4GAun7sbA6ksB8ncDqfnwu83CfxmfFjRPSb4GX7tbgbOZG/jaubZ5FyCnE407o+bR4LFtt1hlBcjK0CDwVP+gdB04t89/1O/w1cDnyilFU='

line_bot_api = LineBotApi(channel_access_token) ##ตัวส่งapi
handler = WebhookHandler(channel_secret)

### database ชั่วคราว
Card = [] ### บัตรสำหรับเข้าเรียน
Member = [] ### บัตรสมาชิค


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
    text_fromUser = event.message.text ### ข้อความจาก ยูสเซอ line
    print(text_fromUser)

    #### ตรวจสอบ ว่า ภายในข้อความของยูส มีคำว่า เช็คราคา อยู่หรือไม่ ถ้าใช้ บอทจะตอบกลับเป็น flex message
    if 'เช็คราคา' in text_fromUser:
        from Resource.bxAPI import GetBxPrice
        from random import randint
        num = randint(1,10)
        data = GetBxPrice(Number_to_get=num) ## เก็บจำนวนข้อมูล

        from Resource.FlexMessage import setbubble , setCarousel

        flex = setCarousel(data)


        flex = SetMenuMessage_Object(flex)
        send_flex(Reply_token,file_data = flex,bot_access_key = channel_access_token)

    ##### check newsapi
    elif 'เช็คข่าวสาร' in text_fromUser:
        text = TextSendMessage(text='ท่านได้ทำการเลือกเมนู เช็คข่าวสาร') #setup text message
        
        from Resource.FlexMessage import news_setbubble 
        from Resource.GetNews import get_cnn_news

        data = get_cnn_news()
        print(data)
        flex = news_setbubble(data['title'],data['description'],data['url'],data['image_url'])
        
        text = TextSendMessage(text='รายงานข่าวสารสำหรับ CNN ล่าสุด').as_json_dict()

        msg = SetMenuMessage_Object([text,flex])

        r = send_flex(Reply_token,file_data = msg,bot_access_key = channel_access_token)
        print(r.content)


    elif 'บัตรสมาชิก' in text_fromUser:
        text = TextSendMessage(text='กรุณาแสดงบัตรให้แก่สตาฟ').as_json_dict()
        from MessageTemplate.Imgmap import MemberCard , confirmRegis
        flex1 = MemberCard()
        flex2 = confirmRegis()
        msg = SetMenuMessage_Object([text,flex2,flex1])
        send_flex(Reply_token,file_data = msg,bot_access_key = channel_access_token)
    

    ### กรณีเข้ามาเอาบัตรนักเรียน
    elif 'บัตรนักเรียน' in text_fromUser :
        uid = event.source.user_id
        found = False
        for i in Card:
            if i['uid'] == str(uid):
                from MessageTemplate.Imgmap import GetStudentCard
                flex = SetMenuMessage_Object(GetStudentCard(i['courses']))
                send_flex(Reply_token,file_data = flex,bot_access_key = channel_access_token)
                found = True
                break
                ### found หาเจอแล้ว

        if found is False:
            text = TextSendMessage(text='กรุณาสมัคร/ลงทะเบียนคลาสเรียน กดเมนูด้านล่างเพื่อลงทะเบียน').as_json_dict()
            from MessageTemplate.Imgmap import PleaseRegister
            msg = PleaseRegister()
            flex = SetMenuMessage_Object([text,msg])
            send_flex(Reply_token,file_data = flex,bot_access_key = channel_access_token)


    else:
        
        message = '' ### message ที่เราจะส่งกลับไปให้ยูสเสอ
        text = []
        user_data = None

        from dialogflow_uncle import detect_intent_texts
        project_id = os.getenv('DIALOGFLOW_PROJECT_ID')
        session_id = event.source.user_id  ## get user id
        message = detect_intent_texts(project_id,session_id,text_fromUser,'th')
        

        for i in message['fulfillment_messages']:### เพิ่มจากในคลิบ
            txt = TextSendMessage(text=i)### เพิ่มจากในคลิบ
            text.append(txt)### เพิ่มจากในคลิบ

        


        
        ## adding imagemap message เรียนอะไร
        if message['action'] == 'Uncleregister':
            from MessageTemplate.Imgmap import selectCourse
            imagemap = Base.get_or_new_from_json_dict(selectCourse(),ImagemapSendMessage)
            text.append(imagemap)
            ### prepare imagemap message to send 

        #### เรียนที่ไหน
        elif message['action'] == 'Uncleregister.Uncleregister-custom':
            from MessageTemplate.Imgmap import selectWhere
            imagemap = Base.get_or_new_from_json_dict(selectWhere(),ImagemapSendMessage)
            text.append(imagemap)
            ### prepare Imagemap message to send

        ### ให้ยูสเซอลงเวลา
        elif message['action'] == 'Uncleregister.Uncleregister-custom.Uncleregister-courses-custom':
            from MessageTemplate.Imgmap import selectTime
            msg = Base.get_or_new_from_json_dict(selectTime(),TemplateSendMessage)
            text.append(msg)

        #### confirm message
        elif message['action'] == 'Uncleregister.Uncleregister-custom.Uncleregister-courses-custom.Uncleregister-courses-where-custom':
            from MessageTemplate.Imgmap import confirmRegis
            msg = Base.get_or_new_from_json_dict(confirmRegis(),TemplateSendMessage)
            text.append(msg)
        

        ### sumarize message
        elif message['action'] == 'Uncleregister.Uncleregister-custom.Uncleregister-courses-custom.Uncleregister-courses-where-custom.Uncleregister-courses-where-when-yes':
            from google.protobuf.json_format import MessageToDict
            data = message['parameters']
            data = MessageToDict(data)


            from MessageTemplate.Imgmap import GetStudentCard


            ####เนื้องจากการส่งข้อความแบบ flex2019 SDK python ยังไม่รองรับทำให้เราต้องกลับมาส่งแบบ manual
            msg = []
            for i in text:
                Dict = i.as_json_dict()
                msg.append(Dict)
            msg.append(GetStudentCard(data['courses']))
            flex = SetMenuMessage_Object(msg)
            send_flex(Reply_token,file_data = flex,bot_access_key = channel_access_token)
            
            ### Keep data to database
            data = {
                'uid':session_id,
                'month':data['month'],
                'where':data['where'],
                'courses':data['courses']
            }
            Card.append(data)

            print(Card)

        #### กรณีบอท ตอบคำถามกลับไป
        
        elif message['action'] == 'BotChallenge.BotChallenge-fallback':
            from MessageTemplate.Imgmap import AnwserMsg

            from Resource.wolf import search_wiki

            result = search_wiki(text_fromUser)

            ### set msg + answer
            Flex_Ans = AnwserMsg(text_fromUser,result)

            ### set quick reply
            qbtn = QuickReplyButton(image_url='https://cdn0.iconfinder.com/data/icons/online-education-butterscotch-vol-2/512/Questions_And_Answers-512.png'
            ,action=MessageAction('หยุดถาม','หยุดถาม'))
            q = QuickReply(items=[qbtn])

            ### set text as json
            new_text1 = TextSendMessage(text='ลุงขอหาแปรป...').as_json_dict()
            new_text2 = TextSendMessage(text='อยากถามต่อไหม ถ้าไม่... กดปุ่ม หยุดถามได้เลยจร้า',quick_reply=q).as_json_dict()

            ### send msg with quick reply
            flex = SetMenuMessage_Object(Message_data=[new_text1,Flex_Ans,new_text2])

            r = send_flex(Reply_token,file_data = flex,bot_access_key = channel_access_token)
            print(r.content)

            
        print(message['action'])

        ### ตอบตามที่ dialogflow ส่งกลับมาให้
        line_bot_api.reply_message(Reply_token,messages=text)

        
        



@handler.add(FollowEvent)
def RegisRichmenu(event):
    userid = event.source.user_id
    disname = line_bot_api.get_profile(user_id=userid).display_name
    ### setup quick reply button
    button_1 = QuickReplyButton(action=MessageAction(label='เช็คราคา',text='เช็คราคา'))
    button_2 = QuickReplyButton(action=MessageAction(label='เช็คข่าวสาร',text='เช็คข่าวสาร'))
    button_3 = QuickReplyButton(action=MessageAction(label='สมัครเรียนไพทอนกับลุง',text='สนใจคอสเรียนไพทอน'))

    qbtn = QuickReply(items=[button_1,button_2,button_3])
    ### text message object
    text = TextSendMessage(text='สวัสดีคุณ  {}  ยินดีต้อนรับสู่บริการแชทบอท'.format(disname))
    text_2 = TextSendMessage(text='กรุณาเลือกเมนูที่ท่านต้องการ',quick_reply = qbtn)
    ### link richmenu
    line_bot_api.link_rich_menu_to_user(userid,'richmenu-32639ff3723a0284a8a8e2f59eed2a99')
    ### reply message when user follow
    line_bot_api.reply_message(event.reply_token,messages=[text,text_2])

### รับ date time picker
@handler.add(PostbackEvent)
def GetPostback(event):
    Reply_token = event.reply_token
    text_fromUser = event.postback.params['datetime']
    print(text_fromUser)

    month = int(text_fromUser[5:7])
    print(month)

    import datetime

    monthinteger = month

    month = str(datetime.date(1900, monthinteger, 1).strftime('%B'))

    print (month)

    message = '' ### message ที่เราจะส่งกลับไปให้ยูสเสอ
    from dialogflow_uncle import detect_intent_texts
    project_id = os.getenv('DIALOGFLOW_PROJECT_ID')
    session_id = event.source.user_id  ## get user id
    message = detect_intent_texts(project_id,session_id,month,'en')
    
    text = []
    user_data = None

    for i in message['fulfillment_messages']:### เพิ่มจากในคลิบ
        txt = TextSendMessage(text=i)### เพิ่มจากในคลิบ
        text.append(txt)### เพิ่มจากในคลิบ
    
    if message['action'] == 'Uncleregister.Uncleregister-custom.Uncleregister-courses-custom.Uncleregister-courses-where-custom':
        from MessageTemplate.Imgmap import summary_msg
        data = message['parameters']
        from google.protobuf.json_format import MessageToDict
        data = MessageToDict(data)
        when = data['month']
        where = data['where']
        course = data['courses']
        msg = Base.get_or_new_from_json_dict(summary_msg(when,where,course),FlexSendMessage)
        text.append(msg)### เพิ่มจากในคลิบ
    


    res = line_bot_api.reply_message(Reply_token,messages=text)





### serve imagemap
@app.route('/MessageTemplate/<PICNAME>/1040')
def getpicbyname(PICNAME):
    print('PIC : ' + PICNAME)
    path = 'MessageTemplate'
    return send_from_directory(path,PICNAME)

### serve simple image
@app.route('/MessageTemplate/<PICNAME>')
def getpicbyname_static(PICNAME):
    print('PIC : ' + PICNAME)
    path = 'MessageTemplate'
    return send_from_directory(path,PICNAME)


if __name__ == "__main__":
    os.environ['DIALOGFLOW_PROJECT_ID'] = 'uncletut01-tsijhr'
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'Credentials.json'
    app.run(port=200)
    #heroku cloud server https://uncletut01.herokuapp.com//webhook




