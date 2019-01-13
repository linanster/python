#! /usr/bin/python
# coding:utf8
#

from url_manager import UrlManager
from html_downloader import HtmlDownloader
from html_parser import HtmlParser
from html_outputer import HtmlOutputer

class SpiderMain(object):
    def __init__(self):
	self.urls = UrlManager()
	self.downloader = HtmlDownloader()
	self.parser = HtmlParser()
	self.outputer = HtmlOutputer()    

    def craw(self, url):
	count = 1
	self.urls.add_new_url(url)
	while self.urls.has_new_url():
	    try:
		new_url = self.urls.get_new_url()
		html_cont = self.downloader.download(new_url)
		new_urls,html_data = self.parser.parse(new_url, html_cont)
		self.urls.add_new_urls(new_urls)
		self.outputer.collect_data(html_data)
		print "%d craw success : %s" % (count, new_url)
		if count >= 10:
		    break
		count = count + 1
	    except Exception as e:
		print str(e)
		print "%d craw failed : %s" % (count, new_url)
	self.outputer.output()

if __name__ == "__main__":
    root_url = "https://baike.baidu.com/item/Python/407313"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
