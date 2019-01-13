#! /usr/bin/python
# coding:utf8
#
import bs4
import re
import urlparse

class HtmlParser(object):
    def __init__(self):
	pass

    def _get_html_data(self, url, soup):
	data = {}
	# url
	data['url'] = url
	# 标题 
	# <dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1> </dd>
	title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find('h1')
	data['title'] = title_node.get_text()
	# 简介 
	# <div class="lemma-summary" label-module="lemmaSummary">
	# <div class="para" label-module="para">Python是一种计算机程序设计语言。</div>
	# </div>
	summary_node = soup.find('div', class_="lemma-summary").find('div')
	data['summary'] = summary_node.get_text()
	return data
	
    def _get_new_urls(self, soup):
	new_urls = set()
	# /item/....[/...]
	links = soup.find_all('a', href=re.compile(r"/item/[/%A-z]+"))
	for link in links:
	    new_url_suffix = link['href']
	    new_url_full = urlparse.urljoin("http://baike.baidu.com", new_url_suffix)
	    new_urls.add(new_url_full)
	return new_urls

    def parse(self, url, html):
	if url is None or html is None:
	    return
	soup = bs4.BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
	new_data = self._get_html_data(url, soup)
	new_urls = self._get_new_urls(soup)
	return new_urls, new_data


