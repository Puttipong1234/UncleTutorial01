richdata = {
  "size": {
    "width": 2500,
    "height": 1686
  },
  "selected": True,
  "name": "Rich Menu 1",
  "chatBarText": "Bulletin",
  "areas": [
    {
      "bounds": {
        "x": 0,
        "y": 8,
        "width": 1664,
        "height": 837
      },
      "action": {
        "type": "message",
        "text": "สนใจคอสเรียนไพทอน"
      }
    },
    {
      "bounds": {
        "x": 1672,
        "y": 8,
        "width": 811,
        "height": 828
      },
      "action": {
        "type": "message",
        "text": "ขอบัตรนักเรียนหน่อยครับ"
      }
    },
    {
      "bounds": {
        "x": 17,
        "y": 853,
        "width": 802,
        "height": 811
      },
      "action": {
        "type": "message",
        "text": "เช็คราคา"
      }
    },
    {
      "bounds": {
        "x": 845,
        "y": 853,
        "width": 802,
        "height": 811
      },
      "action": {
        "type": "message",
        "text": "เช็คข่าวสาร"
      }
    },
    {
      "bounds": {
        "x": 1672,
        "y": 870,
        "width": 820,
        "height": 798
      },
      "action": {
        "type": "message",
        "text": "ไหนขอทดสอบความรู้หน่อยซิ"
      }
    }
  ]
}

from app import channel_access_token

import json

import requests



def RegisRich(Rich_json,channel_access_token):

    url = 'https://api.line.me/v2/bot/richmenu'

    Rich_json = json.dumps(Rich_json)

    Authorization = 'Bearer {}'.format(channel_access_token)


    headers = {'Content-Type': 'application/json; charset=UTF-8',
    'Authorization': Authorization}

    response = requests.post(url,headers = headers , data = Rich_json)

    print(str(response.json()['richMenuId']))

    return str(response.json()['richMenuId'])

def CreateRichMenu(ImageFilePath,Rich_json,channel_access_token):


    richId = RegisRich(Rich_json = Rich_json,channel_access_token = channel_access_token)

    url = ' https://api.line.me/v2/bot/richmenu/{}/content'.format(richId)

    Authorization = 'Bearer {}'.format(channel_access_token)

    headers = {'Content-Type': 'image/jpeg',
    'Authorization': Authorization}

    img = open(ImageFilePath,'rb').read()

    response = requests.post(url,headers = headers , data = img)

    print(response.json())



CreateRichMenu(ImageFilePath='Resource/uncletut01.jpg',Rich_json=richdata,channel_access_token=channel_access_token)


