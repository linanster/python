#! /usr/bin/python
# coding:utf8
#
class UrlManager(object):
    def __init__(self):
	self.urls_old = set()
	self.urls_new = set()

    def add_new_url(self, url):
	if url is None:
	    return
	if url not in self.urls_old and url not in self.urls_new:
	    self.urls_new.add(url)

    def add_new_urls(self, urls):
	if urls is None or len(urls) == 0:
	    return
	for url in urls:
	    self.add_new_url(url)

    def has_new_url(self):
	return len(self.urls_new) != 0

    def get_new_url(self):
	url = self.urls_new.pop()
	self.urls_old.add(url)
	return url
