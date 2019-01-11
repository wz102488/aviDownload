# -*- coding:utf-8 -*-
import requests

#下载网页内容
class htmlDownloader(object):
    def download(self, url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
        }
        if url is None:
            return None
        r = requests.get(url, headers=headers)
        a = r.text
        return a