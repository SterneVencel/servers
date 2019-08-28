#!/bin/python3
from datetime import date
from datetime import timedelta
import time
import os

class PreferredStock():
    def __init__ (self):
        pass
    
    def preferred_stock_file (self):
        today = date.today()
        n = 1
        while True:
            target_date = today - timedelta(days=n)
            #print (str(target_date) + str(type(target_date)))
            week = str(target_date.strftime("%A"))[:3]
            file_name = str(target_date) + "-" + week + ".txt"
            file_path = '/export/servers/shell/preferred_stock_for_downside_forecast_algo/{}'.format(file_name)
            if os.path.exists(file_path) == True:
                #print (file_path)
                return file_path
                break
            else:
                n = n + 1
                continue
    def preferred_stock_gid(self):
         file = self.preferred_stock_file()
         stock_gid_list = []
         with open(file, 'rt') as f:
             while True:
                 line = f.readline().strip('\n')
                 if not line:
                     break
                 stock_gid_list.append(line)
         #函数返回一个列表
         return stock_gid_list

if __name__ == '__main__':
    preferred_stock_obj = PreferredStock()
    stock_gid_list=preferred_stock_obj.preferred_stock_gid()
    print(stock_gid_list)
    
    
