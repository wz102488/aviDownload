# -*- coding:utf-8 -*-
#这是主文件
import html_download
import html_outputer
import html_parser
import url_manager


class spiderMain(object):
#初始化
    def __init__(self):
        self.urls = url_manager.urlManager()
        self.downloader = html_download.htmlDownloader()
        self.parser = html_parser.htmlParser()
        self.outPuter = html_outputer.htmlOutPuter()

    def craw(self, root_url):
        self.urls.add_new_url(root_url)                                      #将root_url添加进new url
        while self.urls.has_new_url():                                       #如果new url不为空，则循环
            try:
                new_url = self.urls.get_new_url()                            #获取new url
                html_cont = self.downloader.download(new_url)                #获取网页内容
                new_urls, new_data = self.parser.paeser(new_url, html_cont)  #获取筛选的页面url和筛选的视频下载信息
                self.urls.add_new_urls(new_urls)                             #将url传给url管理器
                self.outPuter.collect_data(new_data)                         #将下载信息传给outPuter
            except:
                print("craw faild!")

if __name__ == "__main__":
    root_url = "http://www.caca001.com"
    obj_spider = spiderMain()
    obj_spider.craw(root_url)

