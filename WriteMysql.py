#!/bin/python3
#coding = utf-8
import os
import re
import pymysql
import time

class WriteMysql():
    def __init__(self,mysql_conf):
        #接收的是一个配置，格式为dict
        self.mysql_conf = mysql_conf
    def connection_mysql(self):
        conn = pymysql.connect(**self.mysql_conf)
        return conn
    def create_cursor(self, conn_obj):
        cur = conn_obj.cursor()
        return cur
    def create_table(self,cur_obj,table_name):
        cur_obj.execute("SHOW TABLES")
        table_tuple=cur_obj.fetchall()
        tag = 0
        for sub_tuple in table_tuple:
            if table_name in sub_tuple:
                tag = 1
                return table_name
                break
            else:
                continue
        if tag == 0:
            cur_obj.execute("CREATE TABLE IF NOT EXISTS {table_name} (id INT AUTO_INCREMENT PRIMARY KEY)".format(table_name=table_name))
            return table_name
    def insert_data(self, conn_obj, cur_obj, table_name, stock_real_time_info_dict):
        buyThreePri = stock_real_time_info_dict["buyThreePri"]
        sellTwoPri = stock_real_time_info_dict["sellTwoPri"]
        sellTwo = stock_real_time_info_dict["sellTwo"]
        todayStartPri = stock_real_time_info_dict["todayStartPri"]
        competitivePri = stock_real_time_info_dict["competitivePri"]
        sellOne = stock_real_time_info_dict["sellOne"]
        sellFourPri = stock_real_time_info_dict["sellFourPri"]
        buyThree = stock_real_time_info_dict["buyThree"]
        traAmount = stock_real_time_info_dict["traAmount"]
        sellFivePri = stock_real_time_info_dict["sellFivePri"]
        buyFivePri = stock_real_time_info_dict["buyFivePri"]
        time = stock_real_time_info_dict["time"]
        buyOnePri = stock_real_time_info_dict["buyOnePri"]
        yestodEndPri = stock_real_time_info_dict["yestodEndPri"]
        sellFour = stock_real_time_info_dict["sellFour"]
        date = stock_real_time_info_dict["date"]
        reservePri = stock_real_time_info_dict["reservePri"]
        nowPri = stock_real_time_info_dict["nowPri"]
        buyFour = stock_real_time_info_dict["buyFour"]
        buyFourPri = stock_real_time_info_dict["buyFourPri"]
        todayMax = stock_real_time_info_dict["todayMax"]
        name = stock_real_time_info_dict["name"]
        todayMin = stock_real_time_info_dict["todayMin"]
        buyFive = stock_real_time_info_dict["buyFive"]
        sellFive = stock_real_time_info_dict["sellFive"]
        sellThree = stock_real_time_info_dict["sellThree"]
        buyOne = stock_real_time_info_dict["buyOne"]
        increPer = stock_real_time_info_dict["increPer"]
        traNumber = stock_real_time_info_dict["traNumber"]
        increase = stock_real_time_info_dict["increase"]
        buyTwo = stock_real_time_info_dict["buyTwo"]
        buyTwoPri = stock_real_time_info_dict["buyTwoPri"]
        gid = stock_real_time_info_dict["gid"]
        sellThreePri = stock_real_time_info_dict["sellThreePri"]
        sellOnePri = stock_real_time_info_dict["sellOnePri"] 
        with conn_obj:
            sql = "INSERT INTO {table_name} (todayMax, gid, reservePri, traAmount, nowPri, buyFive, time, sellOne, date, increPer, sellTwoPri, todayMin, buyFour, buyTwoPri, buyTwo, traNumber, sellFivePri, name, buyThreePri, sellFive, sellThreePri, competitivePri, buyThree, sellTwo, sellThree, increase, sellFour, buyOnePri, todayStartPri, buyFourPri, yestodEndPri, sellOnePri, buyOne, sellFourPri, buyFivePri) VALUES ('{todayMax}', '{gid}', '{reservePri}', '{traAmount}', '{nowPri}', '{buyFive}', '{time}', '{sellOne}', '{date}', '{increPer}', '{sellTwoPri}', '{todayMin}', '{buyFour}', '{buyTwoPri}', '{buyTwo}', '{traNumber}', '{sellFivePri}', '{name}', '{buyThreePri}', '{sellFive}', '{sellThreePri}', '{competitivePri}', '{buyThree}', '{sellTwo}', '{sellThree}', '{increase}', '{sellFour}', '{buyOnePri}', '{todayStartPri}', '{buyFourPri}', '{yestodEndPri}', '{sellOnePri}', '{buyOne}', '{sellFourPri}', '{buyFivePri}')"
            cur_obj.execute(sql.format(table_name=table_name, yestodEndPri=yestodEndPri, traAmount=traAmount, todayMax=todayMax, sellTwo=sellTwo, buyFive=buyFive, sellThreePri=sellThreePri, sellOne=sellOne, buyFourPri=buyFourPri, buyOnePri=buyOnePri, time=time, sellFour=sellFour, nowPri=nowPri, increPer=increPer, reservePri=reservePri, sellOnePri=sellOnePri, competitivePri=competitivePri, traNumber=traNumber, buyFour=buyFour, buyFivePri=buyFivePri, name=name, todayStartPri=todayStartPri, buyTwoPri=buyTwoPri, sellFivePri=sellFivePri, sellThree=sellThree, sellTwoPri=sellTwoPri, date=date, sellFive=sellFive, buyOne=buyOne, sellFourPri=sellFourPri, buyThree=buyThree, buyThreePri=buyThreePri, buyTwo=buyTwo, gid=gid, todayMin=todayMin, increase=increase))
    
    def alter_column(self,cur_obj, table_name):
        float_key = {'FLOAT(5)':['increase', 'nowPri','todayMin', 'competitivePri','todayMax','yestodEndPri','reservePri','sellFourPri', 'sellThreePri', 'todayStartPri','sellFivePri','increPer', 'sellOnePri', 'sellTwoPri','buyThreePri', 'buyFourPri', 'buyFivePri', 'buyOnePri','buyTwoPri',]}
        int_key = {'INT(8)':['buyFive','buyFour','buyThree','buyTwo','buyOne','sellOne','sellFour', 'sellFive','sellThree','sellTwo']}
        bigint_key = {'BIGINT(20)':['traAmount','traNumber']}
        date_key = {'DATE':['date']}
        time_key = {'TIME':['time']}
        varchar_key = {'VARCHAR(20)':['name','gid']}
        format_key_list = [float_key, int_key, bigint_key, date_key, time_key, varchar_key]  

        for key in format_key_list:
            for field in list(key.values())[0]:
                format_key = list(key.keys())[0] 
                sql = "ALTER TABLE {table_name} ADD COLUMN {field} {format_key} DEFAULT NULL".format(table_name=table_name, field=field, format_key=format_key)
                cur_obj.execute(sql)

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
    
