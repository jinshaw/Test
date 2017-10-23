#-*- coding: utf-8 -*-
import MySQLdb

def insert_One():
    try:
        conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='server',db='test2017')
    except:
        print u'连接mysql数据库失败'
    else:
        conn
