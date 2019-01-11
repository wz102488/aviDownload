# -*- coding:utf-8 -*-
#分析页面
import re
from bs4 import BeautifulSoup

class htmlParser(object):
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile("videos"))           #选取标签为a，href包含videos的标签
        for link in links:
            new_url = link['href']                                      #获取链接地址
            new_urls.add(new_url)                                       #存储链接
        #print(new_urls)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}
        title_node = soup.find('head').find('title')                    #获取网页标题
        urls = soup.find_all('a', href=re.compile(".mp4"))              #查找标签为a，链接包含,mp4的标签

        for url in urls:
            res_data['url'] = url['href']
        res_data['title'] = title_node.get_text()
        print(res_data)
                                                                        # 将下载链接和标题一起返回
        return res_data

    def paeser(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

