#!/bin/python3
# -*- coding: utf-8 -*-
import json, urllib
#from urllib import urlencode
from urllib import parse
from urllib import request
import pymysql
import time
import holiday
#----------------------------------
# 股票数据调用示例代码 － 聚合数据
# 在线接口文档：http://www.juhe.cn/docs/21
#----------------------------------

class JuheAPI():
    def __init__(self):
        pass

    def juhe_config(self):
        #需要配置聚合账号的APPkey
        appkey = "7549c2fbdc4b16b0b2f251d9f900dc8e"
        #聚合数据股市数据的URL，只针对沪深实时股票数据
        url = "http://web.juhe.cn:8080/finance/stock/hs"
        return appkey,url
        
    def stock_gid_request(self, stock_gid):
        appkey = self.juhe_config()[0]
        url = self.juhe_config()[1]
        method = 'GET'
        #URL请求参数配置，gid指股票代码
        params = {"gid": stock_gid, "key": appkey}
        params = parse.urlencode(params)
        if method == "GET":
            f = request.urlopen("%s?%s" % (url, params))
        else:
            f = urllib.urlopen(url, params)     
        content_bytes = f.read()
        #print (content_bytes)
        content_unicode=content_bytes.decode('utf-8')
        content_dict = json.loads(content_unicode)
        if content_dict:
            error_code = content_dict["error_code"]
            if error_code == 0:
                #打印的是个dict
                return (0, content_dict["result"][0]['data'])
            else:
                return (1, "%s:%s" % (content_dict["error_code"],content_dict["reason"]))
        else:
            return (2, "request api error")
    def intervel_collect_tactics(self, stock_gid):
        appkey = self.juhe_config()[0]
        url = self.juhe_config()[1]
        method = 'GET'
        self.stock_gid_request(appkey, url, method, stock_gid)
        
if __name__ == '__main__':
   stock_gid = "sz002263"
   stock =  JuheAPI()
   t = stock.stock_gid_request(stock_gid)
   print(t)
