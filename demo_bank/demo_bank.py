#! /usr/bin/python
# coding:utf8

import sys
import MySQLdb

class TransferMoney(object):
    def __init__(self,conn):
	self.conn = conn

    def check_account_exist(self, name):
	cursor = self.conn.cursor()
	try:
	    sql = 'SELECT * FROM tb_account WHERE name="%s"' % name
	    cursor.execute(sql)
	    result = cursor.fetchall()
	    if len(result) != 1:
		raise Exception("账户 %s 不存在" % name)
	finally:
	    cursor.close()

    def has_enough_money(self, name, money):
	cursor = self.conn.cursor()
	try:
	    sql = 'SELECT * FROM tb_account WHERE name="%s" and money>%s' % (name,money)
	    cursor.execute(sql)
	    result = cursor.fetchall()
	    if len(result) != 1:
		raise Exception("账户 %s 余额不足 %s 元" % (name, money))
	finally:
	    cursor.close()

    def reduce_money(self, name, money):
	cursor = self.conn.cursor()
	try:
	    sql = 'UPDATE tb_account SET money=money-%s WHERE name="%s"' % (money, name)
	    cursor.execute(sql)
	    if cursor.rowcount != 1:
		raise Exception("账户 %s 扣款 %d 元失败" % (name, money))
	finally:
	    cursor.close()

    def add_money(self, name, money):
	cursor = self.conn.cursor()
	try:
	    sql = 'UPDATE tb_account SET money=money+%s WHERE name="%s"' % (money, name)
	    cursor.execute(sql)
	    if cursor.rowcount != 1:
		raise Exception("账户 %s 加款 %s 元失败" % (name, money))
	finally:
	    cursor.close()

    def transfer(self, tran_source, tran_target, tran_money):
	try:
	    self.check_account_exist(tran_source)
	    self.check_account_exist(tran_target)
	    self.has_enough_money(tran_source, tran_money)
	    self.reduce_money(tran_source, tran_money)
	    self.add_money(tran_target, tran_money)
	    self.conn.commit()
	except Exception as e:
	    self.conn.rollback()
	    raise e

if __name__ == "__main__":
    tran_source = sys.argv[1]
    tran_target = sys.argv[2]
    tran_money = sys.argv[3]

    conn = MySQLdb.Connect(host='127.0.0.1', user='root', db='bank')
    tran = TransferMoney(conn)

    try:
	tran.transfer(tran_source, tran_target, tran_money)
	print "转账成功: %s 转给 %s 金额 %s 元" % (tran_source, tran_target, tran_money)
    except Exception as e:
	print "转账失败: "+str(e)
    finally:
	conn.close()
