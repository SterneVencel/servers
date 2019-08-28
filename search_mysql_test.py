#!/bin/python3
#coding = utf-8
import os
import re
import pymysql
import time

class SearchMysql():
    def __init__(self,mysql_conf):
        #接收的是一个配置，格式为dict
        self.mysql_conf = mysql_conf
    def connection_mysql(self):
        conn = pymysql.connect(**self.mysql_conf)
        return conn
    def create_cursor(self, conn_obj):
        cur = conn_obj.cursor()
        return cur
    def search_sql(self,table_name,):
        sql = "SELETE * FROM {}"
if __name__ == "__main__":
    mysql_conf = {'host': 'jddb-cn-north-1-5fc2fd87a6144bdb.jcloud.com', 'port': 3306, 'user': 'test_1_rw', 'passwd': 'tgV1xKOowGom864f', 'db': 'teat_1', 'charset': 'utf8'}
    write_mysql = WriteMysql(mysql_conf)
    #print (write_mysql)
    mysql_conn = write_mysql.connection_mysql()
    #print (mysql_conn)
    mysql_conn_cur = write_mysql.create_cursor(mysql_conn)
    #print (mysql_conn_cur)
    #table_new = "test24"
    table_new = write_mysql.create_table(mysql_conn_cur, 'test161')
    #print (table_new)
    alter_table = write_mysql.alter_column(mysql_conn_cur, table_new)
    #print (alter_table)
    stock_real_time_info_dict={'sellThreePri': '0.000', 'yestodEndPri': '15.730', 'buyFourPri': '17.270', 'sellThree': '0', 'sellFour': '0', 'nowPri': '17.300', 'buyFive': '5500', 'competitivePri': '17.300', 'traNumber': '190447', 'sellOnePri': '0.000', 'sellTwo': '0', 'buyTwo': '28900', 'buyFivePri': '17.250', 'buyOnePri': '17.300', 'reservePri': '0.000', 'sellFive': '0', 'traAmount': '322136578.700', 'buyThreePri': '17.280', 'todayMin': '16.100', 'todayStartPri': '16.450', 'todayMax': '17.300', 'sellFourPri': '0.000', 'buyOne': '8953200', 'buyTwoPri': '17.290', 'time': '10:04:06', 'buyThree': '107900', 'date': '2019-04-16', 'sellTwoPri': '0.000', 'sellFivePri': '0.000', 'buyFour': '3300', 'name': '凯龙股份', 'sellOne': '0', 'gid': 'sz002783', 'increase': '1.57', 'increPer': '9.98'}
    insert_info = write_mysql.insert_data(mysql_conn,mysql_conn_cur,table_new,stock_real_time_info_dict)
    
