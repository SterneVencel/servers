#!/bin/python3
# -*- coding: utf-8 -*-
import json, urllib
from urllib import parse
from urllib import request
#from urllib import *
from datetime import date

def api_config(protocol):
    #获取指定日期节假日信息的API来自：http://api.goseek.cn/
    url_http = "http://api.goseek.cn/Tools/holiday"
    url_https = "https://api.goseek.cn/Tools/holiday"
    if protocol == "http":
        return url_http
    if protocol == "https":
        return url_https
def api_available(url):
    #判断API是否可用，返回True可用,返回False不可用
    today = date.today()
    today_str = today.strftime("%Y%m%d")
    url_data = bytes(parse.urlencode({'date': today_str}),encoding = "utf-8")
    try:
        response = request.urlopen(url, url_data)
        response_status = response.getcode()
    except urllib.error.HTTPError as e:
        print (e.code)
        return False
    except urllib.error.URLError as e:
        print (e.code)
        return False
    if response_status == 200:
        return True
    else:
        return False
def date_hosiday_judge(date):
    #导入API配置
    url = api_config('http')
    #判段url是否可用
    avail=api_available(url)
    #判断给定日期是否为节假日
    if avail:
        url_data = bytes(parse.urlencode({'date': date}),encoding = "utf-8")
        try:
            response = request.urlopen(url, url_data)
            response_status = response.getcode()
        except urllib.error.HTTPError as e:
            print (e.code)
        except urllib.error.URLError as e:
            print (e.code)
        if response_status == 200:
            content_bytes = response.read()
            content_unicode = content_bytes.decode('utf-8')
            content_dict = json.loads(content_unicode)
            #返回值为int类型
            #正常工作日对应结果为0,法定节假日对应结果为1,节假日调休补班对应的结果为2,休息日对应结果为 3
            return content_dict['data']
        else:
            print (response_status)
    else:
        print ("http://api.goseek.cn/Tools/holiday unavailable")
       
if __name__ == '__main__':
    #实例参数必须是“20190803”这种格式
    date_hosiday_judge("20190803")
