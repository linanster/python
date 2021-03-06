#! /usr/bin/python
# coding:utf8
#
import MySQLdb
from myclass import HeatMax
from myclass import HeatEndpoints

# 1.收集endpoints信息
try:
    endpoints = HeatEndpoints('/var/www/html/heat_log/download_cisinas03').collect()
    print "收集endpoints完成: "
    print endpoints
    raw_input("\n继续: ")
except Exception as e:
    print "收集endpoints信息错误: " + str(e)
    exit()

# 2.数据库信息
DB_USER = "root"
# DB_HOST = "10.118.252.202"
DB_HOST = "127.0.0.1"
DB_PASSWD = "123456"
DB_DBNAME = "mk"
# DB_DBNAME = "test"
try:
    conn = MySQLdb.Connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWD, db=DB_DBNAME)
except Exception as e:
    print "连接数据库失败: " + str(e)
    exit()

# 3.开始
try:
    tran = HeatMax()
    tran.start(conn, endpoints)
except Exception as e:
    print "运行失败: " + str(e)
else:
    print "运行成功"
finally:
	tran.statistics()
	conn.close()


