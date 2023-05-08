import datetime
from wechatpy import WeChatClient
from wechatpy.client.api import WeChatMessage, WeChatTemplate
import os

#from put import get_course
from put import get_date
from put import get_weather
from put import get_count
from put import get_words
from put import get_random_color
from put import get_birthday
from put import get_jingqi

delter = datetime.timedelta(days=1)  # 与github actions定时任务的延迟日期增量
today = datetime.datetime.now() + delter
jingqi = os.environ['JINGQI']
start_date = os.environ['START_DATE']
city = os.environ['CITY']
birthday = os.environ['BIRTHDAY']


jingqitoday = datetime.datetime.date(datetime.datetime.now() + delter)  # 有增量
zhouqi = 26
laterday = 2


app_id = os.environ["APP_ID"]
app_secret = os.environ["APP_SECRET"]

user_id = os.environ["USER_ID"]
template_id = os.environ["TEMPLATE_ID"]

client = WeChatClient(app_id, app_secret)

wm = WeChatMessage(client)
wea, high, low, temperature = get_weather()
#jingqi_data = get_jingqi('2022-11-08', jingqitoday, 26, 2)
jingqi_data = "1"
words = get_words()
# sure, hidden = get_yq()
'''"sure":{"value":sure, "color":get_random_color()},"hidden":{"value":hidden, "color":get_random_color()},
       "words2":{"value":get_words2(), "color":get_random_color()},'''
data = {"weather": {"value": wea, "color": get_random_color()},
        "temperature": {"value": temperature, "color": get_random_color()},
        "low": {"value": low, "color": get_random_color()}, "high": {"value": high, "color": get_random_color()},
        "love_days": {"value": get_count(), "color": get_random_color()},
        "birthday_left": {"value": get_birthday(), "color": get_random_color()},
        "words": {"value": words, "color": get_random_color()},
        "date": {"value": get_date(), "color": get_random_color()},
        "city": {"value": city, "color": get_random_color()}}
        #"course": {"value": get_course(), "color": get_random_color()},
        "jingqi": {"value": jingqi_data, "color": get_random_color()}}
res = wm.send_template(user_id, template_id, data)
print(res)
