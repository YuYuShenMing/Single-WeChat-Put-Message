import datetime
import math
from wechatpy import WeChatClient
from wechatpy.client.api import WeChatMessage, WeChatTemplate
import requests
import os
import random
import time

delter = datetime.timedelta(days=1)  # 与github actions定时任务的延迟日期增量
today = datetime.datetime.now() + delter
start_date = os.environ['START_DATE']
city = os.environ['CITY']
birthday = os.environ['BIRTHDAY']


# app_id = 'wxb4afc17cd3aafdc6'
# app_secret = 'f39f44b24136158129928cf7de792dc2'
#
# user_id = 'ohLxg5_WDNdN_zoLfiwNBez9awI0'
# template_id = 'NUMnOmRtk_jiCfVX6RtOkD233aZCBS8YqfJKoD7aE64'


# def get_city():
#  return city

def get_course():
    # 课程
    weekindex = today.weekday()
    course = ''
    if weekindex == 1 or weekindex == 4 or weekindex == 6:
        course = "宝~今天要去练声喔~~"
        return course
    return course


def get_date():
    # 当前日期
    #delter = datetime.timedelta(days=1)  # 由于github actions 延迟产生的时差，故+1天
    #date = datetime.datetime.now() + delter
    year = today.year
    month = today.month
    day = today.day
    weeklist = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
    weekindex = today.weekday()
    week = weeklist[weekindex]
    time = str(year) + "年" + str(month) + "月" + str(day) + "日" + " " + str(week)
    return time


# def get_weather():
    # 天气
    # url = "http://autodev.openspeech.cn/csp/api/v2.1/weather?openId=aiuicus&clientType=android&sign=android&city=" + city
#     url = "https://devapi.qweather.com/v7/weather/now?key=381ac2c40914464f8ab6e0520f7d4056&location=101120807"
#     res = requests.get(url).json()
#     weather = res['data']['list'][0]
#     return weather['weather'], math.floor(weather['temp']), math.floor(weather['low']), math.floor(weather['high'])
def get_weather():
    # 天气
    # url = "http://autodev.openspeech.cn/csp/api/v2.1/weather?openId=aiuicus&clientType=android&sign=android&city=" + city
    url1 = "https://devapi.qweather.com/v7/weather/now?key=381ac2c40914464f8ab6e0520f7d4056&location=101280109"
    url2 = "https://devapi.qweather.com/v7/weather/3d?key=381ac2c40914464f8ab6e0520f7d4056&location=101280109"
    res1 = requests.get(url1).json()
    res2 = requests.get(url2).json()
    weather1 = res1['now']
    weather2 = res2['daily'][0]
    # print(weather2['textDay'], weather2['tempMax'], weather2['tempMin'], weather1['temp'])
    return weather2['textDay'], weather2['tempMax'], weather2['tempMin'], weather1['temp']


def get_count():
    # 时间统计
    delta = today - datetime.datetime.strptime(start_date, "%Y-%m-%d")
    return delta.days


def get_birthday():
    # 生日
    next = datetime.datetime.strptime(str(datetime.date.today().year) + "-" + birthday, "%Y-%m-%d")
    if next < today:
        next = next.replace(year=next.year + 1)
    return (next - today).days + 1  # 加1是增量


def get_words():
    # 每日一句
    words = requests.get("https://api.shadiao.pro/chp")
    if words.status_code != 200:
        return get_words()
    return words.json()['data']['text']


# def get_jingqi(momday1, today, zhouqi, tempday):
#     # 经期
#     try:
#         ym = 7
#         mm_year = int(momday1.split("-")[0])
#         mm_month = int(momday1.split("-")[1])
#         mm_day = int(momday1.split("-")[2])
#         momday = datetime.date(mm_year, mm_month, mm_day)  # 当前日期
#         sumdays = str(today.__sub__(momday)).split(" ")[0]  # 距上次日期
#         days = int(int(sumdays) / zhouqi)  # 周期
#         TempDay = tempday * days  # 延迟日期
#         delta = datetime.timedelta(days=days * zhouqi + TempDay)  # 周期及延迟天数增量
#         startday = momday + delta  # 开始日期
#         delta = datetime.timedelta(days=ym - 1)  # 最后一天增量
#         lastday = startday + delta  # 最后一天
#         if startday <= today <= lastday:
#             if today != lastday:
#                 time1 = str(today.__sub__(startday))[0]
#                 mytext = '这几天预计就来姨妈啦~ 今天是预计的第' + str(int(time1) + 1) + '天~ 还要坚持' + \
#                          str(lastday.__sub__(today)).split(" ")[0] + '天哦~'
#             else:
#                 mytext = '姨妈就快要走啦~马上可以愉快地玩耍啦~'
#         else:
#             a = int(str(lastday.__sub__(today)).split(" ")[0]) + 1
#             if a <= 0:
#                 dy = 32 - ym - abs(a)
#             else:
#                 dy = a - ym
#             mytext = '预计下次姨妈还有' + str(dy) + '天~'
#     except Exception as e:
#         mytext = str(e)
#     return mytext
def get_jingqi():
    data = datetime.datetime.now()
    return data

def get_random_color():
    # 颜色
    return "#%06x" % random.randint(0, 0xFFFFFF)

# def get_yq():
#  url = "https://covid.myquark.cn/quark/covid/data?city=" + city
#  yq = requests.get(url).json()
#  yq_data = yq['contryData']
#  return yq_data['local_sure_cnt_incr'], yq_data['hidden_cnt_incr']

# def get_words2():
#  words2 = requests.get('http://open.iciba.com/dsapi/')
#  return words2.json()['note']


# client = WeChatClient(app_id, app_secret)
#
# wm = WeChatMessage(client)
# wea, temperature, low, high = get_weather()
# #sure, hidden = get_yq()
# '''"sure":{"value":sure, "color":get_random_color()},"hidden":{"value":hidden, "color":get_random_color()},
#        "words2":{"value":get_words2(), "color":get_random_color()},'''
# data = {"weather":{"value":wea, "color":get_random_color()},"temperature":{"value":temperature, "color":get_random_color()},
#         "low":{"value":low, "color":get_random_color()},"high":{"value":high, "color":get_random_color()},
#         "love_days":{"value":get_count(), "color":get_random_color()},"birthday_left":{"value":get_birthday(), "color":get_random_color()},
#         "words":{"value":get_words(), "color":get_random_color()}, "date":{"value":get_date(), "color":get_random_color()}, "city":{"value":city, "color":get_random_color()},
#        "course":{"value":get_course(), "color":get_random_color()}}
# res = wm.send_template(user_id, template_id, data)
# print(res)
