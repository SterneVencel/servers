#!/bin/python3
# -*- coding: utf-8 -*-
import datetime

def trading_time():
    today = datetime.date.today()
    preparation_start_timestamp = datetime.datetime.combine(today, datetime.time(9, 00, 00))
    start_timestamp = datetime.datetime.combine(today, datetime.time(9, 30, 00))
    middle_start_timestamp = datetime.datetime.combine(today, datetime.time(11, 30, 00))
    middle_end_timestamp = datetime.datetime.combine(today, datetime.time(13, 00, 00))
    end_timestamp = datetime.datetime.combine(today, datetime.time(15, 00, 00))
    present_time = datetime.datetime.now()

    #0：代表交易时间；1：代表未到交易时间；2：代表中午暂停时间；3：代表今天交易结束
    if present_time < preparation_start_timestamp:
        return 3
    elif present_time >= preparation_start_timestamp and present_time < start_timestamp:
        return 1
    elif (present_time >= start_timestamp and present_time <= middle_start_timestamp):
        return 0
    elif (present_time >= middle_start_timestamp and present_time <= middle_end_timestamp):
        return 2
    elif (present_time >= middle_end_timestamp and present_time <= end_timestamp):
        return 0
    elif present_time > end_timestamp:
        return 3

if __name__ == '__main__':
    print(trading_time())
