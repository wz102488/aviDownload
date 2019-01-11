# -*- coding:utf-8 -*-
#下载文件
import requests


class htmlOutPuter(object):
    def __init__(self):
        pass
    def collect_data(self, data):
        try:
            if data['url'] is None:
                return
        except:
            pass
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
        }
        chunk_size = 1024
        size = 0
        try:
            title = data['title']
            url = data['url']
            print("Downloading :"+title)
        except:
            print("url is None")

        try:
            r = requests.get(url, headers=headers, stream=True, verify=False)
            content_size = int(r.headers['content-length'])
            print(title)
        except:
            print("open file link err")
            return
        try:
            with open('videos/' + title + '.mp4', 'wb') as f:
                for data in r.iter_content(chunk_size=chunk_size):
                    f.write(data)
                    size += len(data)
                    f.flush()
        except:
            print("Download file err")

