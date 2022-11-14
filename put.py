from datetime import date, datetime
import math
from wechatpy import WeChatClient
from wechatpy.client.api import WeChatMessage, WeChatTemplate
import requests
import os
import random
import time


today = datetime.now()
start_date = os.environ['START_DATE']
city = os.environ['CITY']
birthday = os.environ['BIRTHDAY']

# def get_city():
#  return city

def get_course():
    # 课程
    weekindex = datetime.now().weekday()
    course = ''
    if weekindex == 1 or weekindex == 4 or weekindex == 6:
        course = "宝~今天要去练声喔~~"
        return course
    return course


def get_date():
    # 当前日期
    year = datetime.now().year
    month = datetime.now().month
    day = datetime.now().day
    weeklist = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
    weekindex = datetime.now().weekday()
    week = weeklist[weekindex]
    time = str(year) + "年" + str(month) + "月" + str(day) + "日" + " " + str(week)
    return time


def get_weather():
    # 天气
    url = "http://autodev.openspeech.cn/csp/api/v2.1/weather?openId=aiuicus&clientType=android&sign=android&city=" + city
    res = requests.get(url).json()
    weather = res['data']['list'][0]
    return weather['weather'], math.floor(weather['temp']), math.floor(weather['low']), math.floor(weather['high'])


def get_count():
    # 时间统计
    delta = today - datetime.strptime(start_date, "%Y-%m-%d")
    return delta.days


def get_birthday():
    # 生日
    next = datetime.strptime(str(date.today().year) + "-" + birthday, "%Y-%m-%d")
    if next < datetime.now():
        next = next.replace(year=next.year + 1)
    return (next - today).days


def get_words():
    # 每日一句
    words = requests.get("https://api.shadiao.pro/chp")
    if words.status_code != 200:
        return get_words()
    return words.json()['data']['text']


def get_random_color():
    # 时间
    return "#%06x" % random.randint(0, 0xFFFFFF)

# def get_yq():
    # 疫情
#  url = "https://covid.myquark.cn/quark/covid/data?city=" + city
#  yq = requests.get(url).json()
#  yq_data = yq['contryData']
#  return yq_data['local_sure_cnt_incr'], yq_data['hidden_cnt_incr']

# def get_words2():
#  words2 = requests.get('http://open.iciba.com/dsapi/')
#  return words2.json()['note']

