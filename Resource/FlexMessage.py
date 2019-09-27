# Volumn Change Price Prime Secon

# for loop over set Flex and append to carousel
#### set bubble for bxapi
def setbubble(Primary,Secondary,Volumn,Change,Price):
    Change_color = ['#FD7171' if '-' in str(Change) else '#24FF00'][0]
    bubble_data = {
      "type": "bubble",
      "size": "kilo",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "image",
                "url": "https://static.coindesk.com/wp-content/uploads/2017/03/bitcoin-860x430.jpg",
                "size": "full",
                "aspectMode": "cover",
                "aspectRatio": "150:196",
                "gravity": "center",
                "flex": 1
              },
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "text",
                    "text": "HOT PRICE",
                    "size": "xs",
                    "color": "#ffffff",
                    "align": "center",
                    "gravity": "center",
                    "wrap": True
                  }
                ],
                "backgroundColor": "#EC3D44",
                "paddingAll": "2px",
                "paddingStart": "4px",
                "paddingEnd": "4px",
                "flex": 0,
                "position": "absolute",
                "offsetStart": "18px",
                "offsetTop": "18px",
                "cornerRadius": "100px",
                "width": "100px",
                "height": "25px"
              }
            ],
            "height": "200px"
          }
        ],
        "paddingAll": "0px"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "contents": [],
                    "size": "xl",
                    "wrap": True,
                    "text": "{} VS {}".format(Primary,Secondary),
                    "color": "#ffffff",
                    "weight": "bold"
                  },
                  {
                    "type": "text",
                    "text": "PRICE : {} THB".format(Price),
                    "color": "#ffffffcc",
                    "size": "sm"
                  }
                ],
                "spacing": "sm"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "text",
                        "contents": [],
                        "size": "sm",
                        "wrap": True,
                        "margin": "lg",
                        "color": "#ffffffde",
                        "text": "Volumn : {}".format(Volumn)
                      },
                      {
                        "type": "text",
                        "text": "Change : {}".format(Change),
                        "color": "{}".format(Change_color) ##สีเขียว#24FF00 + สีแดง#FF8484 -
                      }
                    ]
                  }
                ],
                "paddingAll": "13px",
                "backgroundColor": "#ffffff1A",
                "cornerRadius": "2px",
                "margin": "xl"
              },
              {
                "type": "button",
                "action": {
                  "type": "uri",
                  "label": "ตรวจสอบกราฟ",
                  "uri": "https://bx.in.th"
                },
                "style": "secondary",
                "margin": "lg"
              }
            ]
          }
        ],
        "paddingAll": "20px",
        "backgroundColor": "#464F69"
      }
    }
    return bubble_data

#### set bubble for newsapi
def news_setbubble(title,description,url,image_url):
  bubble_data = {
  "type": "bubble",
  "size": "giga",
  "hero": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "image",
        "url": image_url,
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "1:1",
        "gravity": "center"
      },
      {
        "type": "image",
        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip15.png",
        "position": "absolute",
        "aspectMode": "fit",
        "aspectRatio": "1:1",
        "offsetTop": "0px",
        "offsetBottom": "0px",
        "offsetStart": "0px",
        "offsetEnd": "0px",
        "size": "full"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "text",
                    "text": title,
                    "size": "xl",
                    "color": "#ffffff",
                    "wrap": True
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "icon",
                    "url": "https://image.flaticon.com/icons/svg/148/148808.svg"
                  },
                  {
                    "type": "icon",
                    "url": "https://image.flaticon.com/icons/svg/148/148808.svg"
                  },
                  {
                    "type": "icon",
                    "url": "https://image.flaticon.com/icons/svg/148/148808.svg"
                  },
                  {
                    "type": "icon",
                    "url": "https://image.flaticon.com/icons/svg/148/148808.svg"
                  },
                  {
                    "type": "icon",
                    "url": "https://image.flaticon.com/icons/svg/149/149732.svg"
                  },
                  {
                    "type": "text",
                    "text": "4.0",
                    "color": "#ffff66"
                  }
                ],
                "spacing": "md"
              }
            ],
            "spacing": "xs"
          }
        ],
        "position": "absolute",
        "offsetBottom": "10%",
        "offsetStart": "0px",
        "offsetEnd": "0px",
        "paddingAll": "20px"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "image",
            "url": "https://cdn1.iconfinder.com/data/icons/metro-ui-dock-icon-set--icons-by-dakirby/512/CNN.png"
          }
        ],
        "position": "absolute",
        "spacing": "xxl",
        "borderWidth": "2px",
        "borderColor": "#FFFFFF",
        "cornerRadius": "20px",
        "width": "50px",
        "offsetTop": "10px",
        "offsetStart": "10px"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "Read More",
              "uri": url
            },
            "style": "secondary",
            "offsetEnd": "-75%"
          }
        ],
        "position": "relative",
        "paddingStart": "32%",
        "paddingEnd": "32%",
        "offsetTop": "-30px"
      }
    ],
    "paddingAll": "0px"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": description,
        "wrap": True,
        "decoration": "none",
        "style": "italic",
        "weight": "regular"
      }
    ],
    "margin": "none"
  }
}
  flexdata = {
    "type": "flex",
    "altText": "Flex Message",
    "contents": ''
    }
  
  flexdata['contents'] = bubble_data
  return flexdata

def setCarousel(data):
    carousel_data = {
    "type": "carousel",
    "contents": []
    }

    flexdata = {
    "type": "flex",
    "altText": "Flex Message",
    "contents": ''
    }

    # loop 
    # for i in getbtc....
    # carousel_data['contents'].append(setbubble(i['prim_name'],......))
    # flexdata[0]['contents'] = carousel_data


    for i in data:
        bubble_data = setbubble(
            Primary = i['prim_name'],
            Secondary = i['sec_name'],
            Volumn = i['volume'],
            Change = i['change'],
            Price= i['last_price']
        )
        carousel_data['contents'].append(bubble_data)
    
    flexdata["contents"] = carousel_data

    return flexdata