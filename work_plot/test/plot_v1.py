#! /usr/bin/python
# coding:utf8
#

from MySQLdb import Connect
import os
import sys
import shutil
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class PlotMain(object):
    def __init__(self, conn, path, key, date1, date2, folder):
	self.conn = conn
	self.path = path
	self.key = 'node_ifs_heat_' + key
	self.date1 = date1
	self.date2 = date2
	self.folder = folder
	self.x = None
	self.y = None

    def sql_x(self):
	"从数据库中查询得到X轴数据"
	sql_format = '''SELECT DATE_FORMAT(op_time_hourly, '%%Y-%%m-%%d:%%H') FROM tb_heat_cisinas03_agg_hourly_rollup WHERE DATE(op_time_hourly) BETWEEN %s AND %s AND op_path=%s AND op_key=%s'''
	sql_key = (self.date1, self.date2, self.path, self.key)
	cursor = self.conn.cursor()
	cursor.execute(sql_format, sql_key)
	temp = cursor.fetchall()
	cursor.close()
	self.x = []
	for t in temp:
	    self.x.append(t[0])

    def sql_y(self):
	"从数据库中查询得到Y轴数据"
	sql_format = '''SELECT op_rate FROM tb_heat_cisinas03_agg_hourly_rollup WHERE DATE(op_time_hourly) BETWEEN %s AND %s AND op_path=%s AND op_key=%s'''
	sql_key = (self.date1, self.date2, self.path, self.key)
	cursor = self.conn.cursor()
	cursor.execute(sql_format, sql_key)
	temp = cursor.fetchall()
	cursor.close()
	self.y = []
	for t in temp:
	    # self.y.append(int(t[0]))
	    # 保留两位小数
	    self.y.append(round(t[0], 2))

    def savepic(self):
	if len(self.x) == 0:
	    pass
	else:
	    # df = pd.DataFrame(self.y, index=self.x)
	    df = pd.DataFrame(self.y, index=range(len(self.x)))
	    ax = df.plot(x_compat=True, grid=True)
	    # ax = df.plot(x_compat=False, grid=True)
	    # ax.set_title(self.key)
	    ax.set_ylabel('op_rate')
	    ax.set_xlabel('time')
	    ax.grid(linestyle="--", alpha=0.3)
	    ax.legend([self.key], loc=0)
	    # plt.show()
	    picname = self.folder + '/' + self.key + '.jpg'
	    # plt.xticks(range(len(self.x)), self.x, rotation = 45)
	    # plt.xticks([])
	    plt.xticks(np.arange(0,len(self.x), step=len(self.x)-1), [self.x[0], self.x[-1]])
	    plt.savefig(picname)

if __name__ == "__main__":
    # 1.数据库信息
    try:
	conn = Connect(host='10.118.252.41', user='root', passwd='123456', db='mk')
    except Exception as e:
	print "连接数据库失败: " + str(e)
	exit()
    else:
	# print "连接数据库成功"
	pass


    path = sys.argv[1]
    date1 = sys.argv[2]
    date2 = sys.argv[3]

    keys = ['blocked', 'contended', 'getattr', 'lock', 'lookup', 'read', 'setattr', 'write', 'rename', 'unlink', 'link']

    folder = date1 + '-' + date2 + '-' + path.replace('/', '-')
    if os.path.exists(folder):
	shutil.rmtree(folder)
    os.mkdir(folder)

    try:
	for key in keys:
	    myplot = PlotMain(conn, path, key, date1, date2, folder)
	    myplot.sql_x()
	    myplot.sql_y()
	    myplot.savepic()
	    # raw_input("P: ")
    except Exception as e:
	print "画图错误: " + str(e)
    finally:
	conn.close()
