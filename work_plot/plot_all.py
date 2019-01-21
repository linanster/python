#! /usr/bin/python
# coding:utf8
#

from myclass import PlotMain, processFolder

dates = [('2018-08-01', '2018-08-16'), ('2018-08-17', '2018-08-22')]
pathes = ['/ifs/cisinas03/projects/PioneerLite', '/ifs/cisinas03/projects2/Cambricon_Thunder', '/ifs/data/Isilon_Support', '/ifs/.ifsvar/upgrade']
keys = ['blocked', 'contended', 'getattr', 'lock', 'lookup', 'read', 'setattr', 'write', 'rename', 'unlink', 'link']

for path in pathes:
    for date in dates:
	date1 = date[0]
	date2 = date[1]
        folder_jpg = processFolder(path, date1, date2)

	try:
	    for key in keys:
		myplot = PlotMain(path, key, date1, date2, folder_jpg)
		myplot.sql_x()
		myplot.sql_y()
		myplot.savepic()
		# raw_input("P: ")
	except Exception as e:
	    print "画图错误: " + str(e)

	
