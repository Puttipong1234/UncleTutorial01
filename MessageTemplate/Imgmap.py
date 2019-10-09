from flask import request
### รูปให้ยูสเซอร์เลือก คอสเรียน
### image/
def selectCourse():
    img_path = '/MessageTemplate/selectCourses.jpg'
    url = 'https://'+request.host+img_path
    print(url)
    imagemap_selectCourse = {
  "type": "imagemap",
  "baseUrl": url,
  "altText": "This is an imagemap",
  "baseSize": {
    "width": 1040,
    "height": 1040
  },
  "actions": [
    {
      "type": "message",
      "area": {
        "x": 440,
        "y": 264,
        "width": 472,
        "height": 164
      },
      "text": "สนใจคอสเรียนเบสิคไพทอน"
    },
    {
      "type": "message",
      "area": {
        "x": 67,
        "y": 464,
        "width": 426,
        "height": 124
      },
      "text": "สนใจคอสเรียนแชทบอท"
    },
    {
      "type": "message",
      "area": {
        "x": 511,
        "y": 560,
        "width": 425,
        "height": 124
      },
      "text": "สนใจคอสเรียนAutomateBot"
    },
    {
      "type": "message",
      "area": {
        "x": 67,
        "y": 702,
        "width": 437,
        "height": 120
      },
      "text": "สนใจคอสเรียน IOT"
    },
    {
      "type": "message",
      "area": {
        "x": 507,
        "y": 797,
        "width": 433,
        "height": 126
      },
      "text": "สนใจคอสเรียนเขียนเว็บด้วยDjango"
    }
  ]
}
    return imagemap_selectCourse

def selectWhere():

    img_path = '/MessageTemplate/selectWhere.jpg'
    url = 'https://'+request.host+img_path

    imagemap = {
  "type": "imagemap",
  "baseUrl": url,
  "altText": "This is an imagemap",
  "baseSize": {
    "width": 1040,
    "height": 1040
  },
  "actions": [
    {
      "type": "message",
      "area": {
        "x": 95,
        "y": 297,
        "width": 643,
        "height": 127
      },
      "text": "เรียนออนไลน์"
    },
    {
      "type": "message",
      "area": {
        "x": 147,
        "y": 470,
        "width": 316,
        "height": 240
      },
      "text": "เรียนออนไลน์"
    },
    {
      "type": "message",
      "area": {
        "x": 569,
        "y": 477,
        "width": 289,
        "height": 298
      },
      "text": "เรียนสดกับลุงวิศวกร"
    },
    {
      "type": "message",
      "area": {
        "x": 329,
        "y": 805,
        "width": 618,
        "height": 126
      },
      "text": "เรียนสดกับลุงวิศวกร"
    }
  ]
}
    return imagemap


import datetime

def selectTime():
    # >>> print(datetime.datetime.now())
    # 2018-07-29 09:17:13.812189
    time = str(datetime.datetime.now()).split()
    date = time[0]
    time = time[1][0:5]

    next_year = str(int(date[0:3]) + 1)
    next_date = str(next_year)+ str(str(datetime.datetime.now())[4:9])

    img_path = '/MessageTemplate/selectTime.jpg'
    url = 'https://'+request.host+img_path


    msg = {
  "type": "template",
  "altText": "this is a buttons template",
  "template": {
    "type": "buttons",
    "actions": [
      {
        "type": "datetimepicker",
        "label": "กดเพื่อเลือกวันเวลา",
        "data": "Data 1",
        "mode": "datetime",
        "initial": "2019-10-09T23:53",
        "max": "2020-10-09T23:53",
        "min": "2018-10-09T23:53"
      }
    ],
    "thumbnailImageUrl": url,
    "title": "กรุณาเลือกช่วงเวลา",
    "text": "เลือกช่วงเวลาที่สะดวก"
  }
}
    return msg


def summary_msg(when,where,course):

    img_path = '/MessageTemplate/uncle.jpg'
    url = 'https://'+request.host+img_path
    course_url = 'https://'+request.host+'/MessageTemplate/course.png'
    calendar_url = 'https://'+request.host+'/MessageTemplate/calendar.png'
    location_url = 'https://'+request.host+'/MessageTemplate/location.png'



    msg = {
  "type": "flex",
  "altText": "Flex Message",
  "contents": {
    "type": "bubble",
    "hero": {
      "type": "image",
      "url": url,
      "size": "full",
      "aspectRatio": "20:13",
      "aspectMode": "cover",
      "action": {
        "type": "uri",
        "label": "Action",
        "uri": "https://www.facebook.com/UncleEngineer"
      }
    },
    "body": {
      "type": "box",
      "layout": "vertical",
      "spacing": "md",
      "action": {
        "type": "uri",
        "label": "Action",
        "uri": "https://www.facebook.com/UncleEngineer"
      },
      "contents": [
        {
          "type": "text",
          "text": "กรุณาตรวจสอบ",
          "size": "xxl",
          "align": "center",
          "weight": "bold",
          "color": "#733E3E"
        },
        {
          "type": "box",
          "layout": "vertical",
          "spacing": "sm",
          "contents": [
            {
              "type": "box",
              "layout": "baseline",
              "contents": [
                {
                  "type": "icon",
                  "url": course_url,
                  "size": "xxl",
                  "aspectRatio": "1:1"
                },
                {
                  "type": "text",
                  "text": "Course เรียน",
                  "margin": "sm",
                  "align": "center",
                  "weight": "bold"
                },
                {
                  "type": "text",
                  "text": course,
                  "size": "sm",
                  "align": "end",
                  "color": "#555555"
                }
              ]
            },
            {
              "type": "box",
              "layout": "baseline",
              "contents": [
                {
                  "type": "icon",
                  "url": location_url,
                  "size": "xxl"
                },
                {
                  "type": "text",
                  "text": "สถานที่เรียน",
                  "margin": "sm",
                  "align": "center",
                  "weight": "bold"
                },
                {
                  "type": "text",
                  "text": where,
                  "size": "sm",
                  "align": "end",
                  "color": "#555555"
                }
              ]
            }
          ]
        },
        {
          "type": "box",
          "layout": "baseline",
          "contents": [
            {
              "type": "icon",
              "url": calendar_url,
              "size": "xxl"
            },
            {
              "type": "text",
              "text": "รอบที่เรียน",
              "margin": "sm",
              "align": "center",
              "weight": "bold"
            },
            {
              "type": "text",
              "text": when,
              "size": "sm",
              "align": "end",
              "color": "#555555"
            }
          ]
        },
        {
          "type": "text",
          "text": "กรุณาตรวจสอบให้ครบถ้วนก่อนกดยืนยันข้อความ หากเกิดข้อผิดพลาด ทางบริษัทจะไม่รับผิดชอบในทุกกรณี",
          "size": "xs",
          "color": "#AAAAAA",
          "wrap": True
        }
      ]
    },
    "footer": {
      "type": "box",
      "layout": "vertical",
      "spacing": "none",
      "margin": "none",
      "contents": [
        {
          "type": "spacer",
          "size": "xs"
        },
        {
          "type": "button",
          "action": {
            "type": "message",
            "label": "CONFIRM",
            "text": "โอเคถูกต้อง"
          },
          "color": "#905C44",
          "style": "primary"
        }
      ]
    }
  }
}
    return msg

def GetStudentCard(course):
    bubble = {
  "type": "bubble",
  "size": "giga",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "filler"
          }
        ],
        "flex": 1,
        "backgroundColor": "#5E5E5E",
        "position": "relative"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "filler"
          }
        ],
        "flex": 3
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://scontent.fbkk5-7.fna.fbcdn.net/v/t1.0-9/48393669_10205485356210511_3832595722780278784_n.jpg?_nc_cat=108&_nc_oc=AQmXpEnez1Rrl0l7E5PuPMN5rBJt01_WC5DqLfmzD1dTHfwsCKwBfqZt1KjH2fCOemU&_nc_ht=scontent.fbkk5-7.fna&oh=cb98dad1047bf334fa9262913a8d83bb&oe=5E3390A4"
          }
        ],
        "position": "absolute",
        "borderColor": "#FFFFFF",
        "borderWidth": "6px",
        "cornerRadius": "70px",
        "offsetStart": "5%",
        "offsetTop": "5%"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "บัตรประจำตัวนักเรียน",
            "color": "#D6D6D6",
            "align": "end"
          },
          {
            "type": "image",
            "url": "https://thaibarcodes.com/wp-content/uploads/sites/169/2013/11/Code-39.jpg",
            "offsetTop": "75px",
            "size": "3xl",
            "offsetEnd": "-5%",
            "aspectMode": "fit",
            "gravity": "center"
          }
        ],
        "position": "absolute",
        "offsetTop": "17%",
        "offsetEnd": "5%",
        "paddingAll": "0px",
        "spacing": "none",
        "width": "100%",
        "height": "100%"
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
                "text": "Name",
                "size": "xxs",
                "margin": "none",
                "color": "#A6A6A6"
              },
              {
                "type": "text",
                "text": "John Doe",
                "margin": "none",
                "size": "sm"
              }
            ],
            "spacing": "none",
            "margin": "none",
            "flex": 1
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "Student ID",
                "size": "xxs",
                "margin": "none",
                "color": "#A6A6A6"
              },
              {
                "type": "text",
                "text": "111-224-236-248",
                "margin": "none",
                "size": "sm"
              }
            ],
            "flex": 1
          }
        ],
        "position": "absolute",
        "offsetStart": "7.5%",
        "offsetTop": "42%",
        "spacing": "xs"
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
                "text": "E-mail",
                "size": "xxs",
                "margin": "none",
                "color": "#A6A6A6"
              },
              {
                "type": "text",
                "text": "Test@gmail.com",
                "margin": "none",
                "size": "sm"
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "Courses",
                "size": "xxs",
                "margin": "none",
                "color": "#A6A6A6"
              },
              {
                "type": "text",
                "text": course,
                "margin": "none",
                "size": "sm"
              }
            ],
            "spacing": "none"
          }
        ],
        "position": "absolute",
        "offsetStart": "55%",
        "offsetTop": "42%",
        "spacing": "xs"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "Uncle Lab",
            "size": "xl",
            "color": "#FFFFFF",
            "align": "end",
            "gravity": "center",
            "flex": 5,
            "offsetTop": "-4px",
            "offsetEnd": "20px",
            "decoration": "none",
            "style": "normal",
            "weight": "regular"
          }
        ],
        "position": "absolute",
        "spacing": "none",
        "margin": "none",
        "paddingAll": "0px",
        "offsetTop": "8%",
        "offsetEnd": "5%",
        "width": "100%"
      },
      {
        "type": "image",
        "url": 'https://'+request.host+'/MessageTemplate/location.png',
        "size": "xxs",
        "flex": 1,
        "position": "absolute",
        "offsetTop": "5%",
        "offsetEnd": "0px"
      }
    ],
    "paddingAll": "0px",
    "height": "280px"
  }
}
    msg = {
  "type": "flex",
  "altText": "Flex Message",
  "contents": {}
    }

    msg['contents'] = bubble

    return msg
    


