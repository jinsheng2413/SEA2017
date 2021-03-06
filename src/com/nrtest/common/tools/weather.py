# -*- coding: utf-8 -*-

"""
@author: 李建方
@license: (C) Copyright 2018, Nari.
@file: weather.py
@time: 2019-04-23 0:48
@desc:
"""

import csv
import datetime
import http.client  # 用做异常处理
import random
import socket  # 用做异常处理
import time

import requests  # 用来抓取网页的html源代码
# 抓取天气网站最近7天的天气情况，写入文件并在控制台显示
from bs4 import BeautifulSoup  # 用来代替正则表达式取源码中相应标签的内容
from pandas.io import json

from com.nrtest.common.utils import Utils


def get_html(url, data=None):
    """
    模拟浏览器来获取网页的html代码
    """
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.235'
    }
    # 设定超时时间，取随机数是因为防止被网站认为是爬虫
    timeout = random.choice(range(80, 180))
    while True:
        try:
            rep = requests.get(url, headers=header, timeout=timeout)
            rep.encoding = "utf-8"
            break
        except socket.timeout as e:
            print("3:", e)
            time.sleep(random.choice(range(8, 15)))

        except socket.error as e:
            print("4:", e)
            time.sleep(random.choice(range(20, 60)))
        except http.client.BadStatusLine as e:
            print("5:", e)
            time.sleep(random.choice(range(30, 80)))

        except http.client.IncompleteRead as e:
            print("6:", e)
            time.sleep(random.choice(range(5, 15)))

    return rep.text


def get_day_weather(html_txt, city_no, city_name):
    final = []
    bs = BeautifulSoup(html_txt, "html.parser")  # 创建BeautifulSoup对象
    body = bs.body  # 获取body部分
    data = body.find("div", {"id": "7d"})  # 找到id为7d的div
    ul = data.find("ul")  # 获取ul部分
    li = ul.find_all("li")  # 获取所有的li

    for day in li:  # 对每个标签中的内容进行遍历
        temp = [city_no, city_name]
        date = day.find("h1").string[:2]  # 获取日期
        if date < Utils.now_str().replace('-', '')[:8][-2:]:
            dt = Utils.str2date(Utils.get_day_range_of_month()[1].replace('-', '')) + datetime.timedelta(days=1)
            date = Utils.date2str(dt)[:6] + date
        else:
            date = Utils.now_str().replace('-', '')[:6] + date

        temp.append(date)  # 将日期添加到temp 中

        inf = day.find_all("p")  # 找到li中的所有p标签
        temp.append(inf[0].string)  # 将第一个p标签中的内容添加到temp列表中红
        if inf[1].find("span") is None:
            temperature_high = None  # 傍晚没有最高气温
        else:
            temperature_high = inf[1].find("span").string  # 最高气温
            temperature_high = temperature_high.replace("℃", "")
        temperature_lower = inf[1].find("i").string  # 找到最低温
        temperature_lower = temperature_lower.replace("℃", "")
        temp.append(temperature_high)
        temp.append(temperature_lower)
        final.append(temp)  # 将temp添加到final中

    return final


def get_hour_weather(html_txt, city_no):
    final = []
    bs = BeautifulSoup(html_txt, "html.parser")  # 创建BeautifulSoup对象
    body = bs.body  # 获取body部分
    all_script = body.find_all("script")
    for script in all_script:
        if script.get_text().find('var observe24h_data') > 0:
            data = script.get_text().strip().replace(' ', '').split('=')[-1][:-1]
            weather = json.loads(data)
            is_next_day = True
            for hour_weather in weather['od']['od2']:
                hw = list(hour_weather.values())
                day = weather['od']['od0'][:8]
                if is_next_day:
                    dt = Utils.str2date(day) + datetime.timedelta(days=1)
                    day = Utils.date2str(dt)
                    is_next_day = not hw[0] == '00'

                hw[0] = day + hw[0] + '0000'
                hw.insert(0, weather['od']['od1'])
                hw.insert(0, city_no)
                final.append(hw)
            final.reverse()
            # '''
            # 'od21' = '23'    23时
            # 'od22' = '18'    温度
            # 'od23' = '72'
            # 'od24' = '东风'   风向
            # 'od25' = '1'     风力
            # 'od26' = '1.7'   降雨量
            # 'od27' = '98'    相对湿度
            # 'od28' = '36'    空气质量
            # '''
    return final[1:]

def write_data(data, name):
    file_name = name
    with open(file_name, 'a', errors='ignore', newline='', encoding='utf-8') as f:
        f_csv = csv.writer(f)
        f_csv.writerows(data)


"""
整点时段信息：
$x('//div[@id="curve"]/div[@class="time"]/em')
整点气温
$x('//div[@id="curve"]/div[@class="tem"]/em')
风向
$x('//div[@id="curve"]/div[@class="winf"]/em')
风力
$x('//div[@id="curve"]/div[@class="winl"]/em')

24小时天气情况
$x('//script[contains(text(),"var observe24h_data")]')


<script type="application/ld+json">
        {
          "@context": "https://ziyuan.baidu.com/contexts/cambrian.jsonld",
          "@id": "https://www.zhihu.com/question/30737616",
          "appid": "否",
          "pubDate": "2015-05-28T08:48:48",
          "upDate": "2016-06-07T11:43:49"
        }</script>        
    pubDate=json.loads(bs.find('script', {'type': 'application/ld+json'}).get_text())["pubDate"]
"""


def get_url():
    city = {
        '唐山': '101090501',
        '秦皇岛': '101091101',
        '廊坊': '101090601',
        '承德': '101090402',
        '张家口': '101090301'
    }
    for k in city:
        print(k)
    city_name = input("请输入你要查询的城市名字：")
    city_num = city[city_name]
    weather_url = "http://www.weather.com.cn/weather/%s.shtml" % city_num
    return weather_url


if __name__ == "__main__":
    city = {
        '唐山': '101090501',
        '秦皇岛': '101091101',
        '廊坊': '101090601',
        '承德': '101090402',
        '张家口': '101090301'
    }
    for city_name, city_no in city.items():
        weather_url = "http://www.weather.com.cn/weather/%s.shtml" % city_no
        html = get_html(weather_url)
        result = get_day_weather(html, city_no, city_name)
        hws = get_hour_weather(html, city_no)
        write_data(result, "weather.csv")
        write_data(hws, "weather.csv")
