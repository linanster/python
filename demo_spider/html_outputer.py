#! /usr/bin/python
# coding:utf8
#
class HtmlOutputer(object):
    def __init__(self):
	self.datas = []

    def collect_data(self, data):
	if data is None:
	    return
	self.datas.append(data)

    def output(self):
	fh = open('output.html', 'w')
	fh.write("<html>\n")
	fh.write("<body>\n")
	fh.write("<table>\n")
	for data in self.datas:
	    fh.write("<tr>\n")
	    fh.write("<td>%s</td>\n" % data['url'])
	    fh.write("<td>%s</td>\n" % data['title'].encode('utf-8'))
	    fh.write("<td>%s</td>\n" % data['summary'].encode('utf-8'))
	    fh.write("/<tr>\n")
	fh.write("/<table>\n")
	fh.write("/<body>\n")
	fh.write("</html>")
	fh.close()

