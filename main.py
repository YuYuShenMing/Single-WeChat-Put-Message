from datetime import date, datetime
import math
from wechatpy import WeChatClient
from wechatpy.client.api import WeChatMessage, WeChatTemplate
import requests
import os
import random
import time

from put import get_course
from put import get_date
from put import get_weather
from put import get_count
from put import get_words
from put import get_random_color
from put import get_birthday

# today = datetime.now()
# start_date = '2022-02-16'
city = '天河区'
# birthday = '12-02'

app_id = 'wxb4afc17cd3aafdc6'
app_secret = 'f39f44b24136158129928cf7de792dc2'

user_id = 'ohLxg5_WDNdN_zoLfiwNBez9awI0'
template_id = 'NUMnOmRtk_jiCfVX6RtOkD233aZCBS8YqfJKoD7aE64'

client = WeChatClient(app_id, app_secret)

wm = WeChatMessage(client)
wea, temperature, low, high = get_weather()
# sure, hidden = get_yq()
'''"sure":{"value":sure, "color":get_random_color()},"hidden":{"value":hidden, "color":get_random_color()},
       "words2":{"value":get_words2(), "color":get_random_color()},'''
data = {"weather": {"value": wea, "color": get_random_color()},
        "temperature": {"value": temperature, "color": get_random_color()},
        "low": {"value": low, "color": get_random_color()}, "high": {"value": high, "color": get_random_color()},
        "love_days": {"value": get_count(), "color": get_random_color()},
        "birthday_left": {"value": get_birthday(), "color": get_random_color()},
        "words": {"value": get_words(), "color": get_random_color()},
        "date": {"value": get_date(), "color": get_random_color()},
        "city": {"value": city, "color": get_random_color()},
        "course": {"value": get_course(), "color": get_random_color()}}
res = wm.send_template(user_id, template_id, data)
print(res)
