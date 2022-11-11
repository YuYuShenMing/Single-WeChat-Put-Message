from datetime import date, datetime
import math
from wechatpy import WeChatClient
from wechatpy.client.api import WeChatMessage, WeChatTemplate
import requests
import os
import random

today = datetime.now()
start_date = os.environ['START_DATE']
city = os.environ['CITY']
birthday = os.environ['BIRTHDAY']

app_id = os.environ["APP_ID"]
app_secret = os.environ["APP_SECRET"]

user_id = os.environ["USER_ID", "USER_IDTWO"]
#user_id_2 = os.environ["USER_IDTWO"]
template_id = os.environ["TEMPLATE_ID"]

def get_city():
  return city

def get_weather():
  url = "http://autodev.openspeech.cn/csp/api/v2.1/weather?openId=aiuicus&clientType=android&sign=android&city=" + city
  res = requests.get(url).json()
  weather = res['data']['list'][0]
  return weather['weather'], math.floor(weather['temp']),math.floor(weather['low']),math.floor(weather['high'])

def get_count():
  delta = today - datetime.strptime(start_date, "%Y-%m-%d")
  return delta.days

def get_birthday():
  next = datetime.strptime(str(date.today().year) + "-" + birthday, "%Y-%m-%d")
  if next < datetime.now():
    next = next.replace(year=next.year + 1)
  return (next - today).days

def get_words():
  words = requests.get("https://api.shadiao.pro/chp")
  if words.status_code != 200:
     return get_words()
  return words.json()['data']['text']

def get_random_color():
  return "#%06x" % random.randint(0, 0xFFFFFF)

#def get_yq():
#  url = "https://covid.myquark.cn/quark/covid/data?city=" + city
#  yq = requests.get(url).json()
#  yq_data = yq['contryData']
#  return yq_data['local_sure_cnt_incr'], yq_data['hidden_cnt_incr']

#def get_words2():
#  words2 = requests.get('http://open.iciba.com/dsapi/')
#  return words2.json()['note']


client = WeChatClient(app_id, app_secret)

wm = WeChatMessage(client)
wea, temperature, low, high = get_weather()
#sure, hidden = get_yq()
data = {"weather":{"value":wea, "color":get_random_color()},"temperature":{"value":temperature, "color":get_random_color()},
        "low":{"value":low, "color":get_random_color()},"high":{"value":high, "color":get_random_color()},
        "love_days":{"value":get_count(), "color":get_random_color()},"birthday_left":{"value":get_birthday(), "color":get_random_color()},
        "words":{"value":get_words(), "color":get_random_color()}, '''"sure":{"value":sure, "color":get_random_color()},"hidden":{"value":hidden, "color":get_random_color()},
       "words2":{"value":get_words2(), "color":get_random_color()},''' "city":{"value":city, "color":get_random_color()}}
res1 = wm.send_template(user_id, template_id, data)
#res2 = wm.send_template(user_id_2, template_id, data)
print(res1)
#print(res2)
