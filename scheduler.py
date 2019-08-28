#!/bin/python3
# -*- coding: utf-8 -*-
import holiday
import realTimeStockDataCollectionbyJuhe as Juhe
import datetime
from datetime import datetime as dt
import time
import multiprocessing
import tradingTime
import os
import WriteMysql
import preferredStock
import subprocess

def trading_day():
    today = datetime.date.today()
    tag = holiday.date_hosiday_judge(today)
    #测试使用
    tag = True
    return tag

class CollProcManager():
    #数据采集实例管理
    def __init__(self):
        pass
    def create_event(self):
        event = multiprocessing.Event()
        #返回值为事件这个obj
        return event
    def collect_process(self, stock_gid, juhe_obj, event):
        print (str(dt.today()) + "  Start build Mysql conn")
        mysql_conf = {'host': 'jddb-cn-north-1-5fc2fd87a6144bdb.jcloud.com', 'port': 3306, 'user': 'test_2_rw',
                      'passwd': 'tgV1xKOowGom864f', 'db': 'test_2', 'charset': 'utf8'}
        write_mysql = WriteMysql.WriteMysql(mysql_conf)
        mysql_conn = write_mysql.connection_mysql()
        print (str(dt.today()) + "  Mysql conn complete")
        mysql_conn_cur = write_mysql.create_cursor(mysql_conn)
        print (str(dt.today()) + "  Creat Mysql cur")
        table_name = 'realtimeinfo'
        while True:
            #print(event.is_set())
            if event.is_set():
                #print(event.is_set())
                print (str(dt.today()) + "  This moment event is True. Start Real-time collect")
                real_time_data = juhe_obj.stock_gid_request(stock_gid)
                if real_time_data[0] == 0:
                    write_mysql.insert_data(mysql_conn, mysql_conn_cur, table_name, real_time_data[1])
                    #今天跌的股票筛选算法
                    if float(real_time_data[1]['increPer']) <= 0:
                        subprocess.getoutput('echo {0}  {1} >> {0}.log'.format(str(datetime.date.today()), real_time_data[1]['gid']))
                        if float(real_time_data[1]['todayMax']) <= float(real_time_data[1]['todayStartPri'])*float(1.05):
                            subprocess.getoutput('echo {0} {1} >> {0}-1.log'.format(str(datetime.date.today()), real_time_data[1]['gid']))
                elif real_time_data[0] == 1:
                    print(real_time_data[1])
                    exit()
                elif real_time_data[0] == 2:
                    print(real_time_data[1])
                    exit()
            else:
                trading_time_judge_int =tradingTime.trading_time()
                if trading_time_judge_int == 3:

                    break
                else:
                    continue
            time.sleep(180)
        return 0

    def collect_proc_manager(self, event, stock_gid_list):
        tag = False
        while True:
            collect_proc_dict = {}
            trading_time_judge_int = tradingTime.trading_time()
            if trading_time_judge_int == 1:
                print (str(dt.today()) + "  <trading_time_judge_int> is 1. Active <create_collect_proc> for every stock_gid")
                collect_proc_dict = self.create_collect_proc(stock_gid_list)
                tag = True
                #print(tag)
                while tag:
                    trading_time_judge_int = tradingTime.trading_time()
                    if trading_time_judge_int == 0:
                        event.set()
                    elif trading_time_judge_int == 2:
                        print (str(dt.today()) + "  <trading_time_judge_int> is 2. Wait <create_collect_proc> for every stock_gid")
                        event.wait()
                    elif trading_time_judge_int == 3:
                        print (str(dt.today()) + "  <trading_time_judge_int> is 3. Stop <create_collect_proc> for every stock_gid")
                        break
                    time.sleep(30)
            elif trading_time_judge_int == 0:
                if len(collect_proc_dict) == 0:
                    collect_proc_dict = self.create_collect_proc(stock_gid_list)
                    tag = True
                #print(tag)
                    while tag:
                        trading_time_judge_int = tradingTime.trading_time()
                        if trading_time_judge_int == 0:
                            event.set()
                        elif trading_time_judge_int == 2:
                            print (str(dt.today()) + "  <trading_time_judge_int> is 2. Wait <create_collect_proc> for every stock_gid")
                            event.wait()
                        elif trading_time_judge_int == 3:
                            print (str(dt.today()) + "  <trading_time_judge_int> is 3. Stop <create_collect_proc> for every stock_gid")
                            break
                        time.sleep(30)
            else:
                time.sleep(5)
                continue

    def create_collect_proc(self,stock_gid_list):
        #print(stock_gid_list)
        print(str(dt.today()) + '  Main Proc ID: ' + str(os.getpid()))
        collect_proc_dict = {}
        for stock_gid in stock_gid_list:
            #print(stock_gid)
            juhe_obj = Juhe.JuheAPI()
            collect_proc_stock_gid = multiprocessing.Process(target=self.collect_process, args=(stock_gid, juhe_obj, event,))
            collect_proc_stock_gid.start()
            collect_proc_dict[stock_gid] = collect_proc_stock_gid
        return collect_proc_dict

def today(date_format):
    #函数返回值为今天的日期格式,"A"为20190407此类格式,"B"为2019-04-07-Sun格式
    today = datetime.date.today()
    #非交易日测试
    today = datetime.date.today() - datetime.timedelta(days=3)
    if date_format == "A":
        today_str = today.strftime('%Y%m%d')
        return today_str
    elif date_format == "B":
        today_str = today.strftime('%Y-%m-%d') + "-" + today.strftime('%A')[:3]
        return today_str
if __name__ == '__main__':
    print (str(dt.today()) + "  Program is running")
    while True:
        if trading_day() == True:
            print (str(dt.today()) + "  Trading Day judge is True")    
            stock_gid_obj = preferredStock.PreferredStock()
            stock_gid_list = stock_gid_obj.preferred_stock_gid()
            print (str(dt.today()) + "  Preferred Stock collect complete")
            controller = CollProcManager()
            print (str(dt.today()) + "  Active CollProcmanager Object complete")
            event = controller.create_event()
            print(str(dt.today()) + "  Create Global event variable complete")
            print(str(dt.today()) + "  Start active coll proc")
            controller.collect_proc_manager(event, stock_gid_list)
        else:
            print (str(dt.today()) + "  Trading Day judge is False")
            time.sleep(60)
