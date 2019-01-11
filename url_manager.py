# -*- coding:utf-8 -*-
#url管理器
class urlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

#若url不为空，并且不在待爬url里，也不在爬过的url里，就把url添加进new urls
    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

#将爬取的页面筛选的新urls添加进待爬urls里
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

#判断有没有待爬url
    def has_new_url(self):
        return len(self.new_urls) != 0

#取出url爬取，然后将放入爬取过的集合
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

