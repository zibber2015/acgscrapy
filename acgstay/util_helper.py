import pycurl
import io
import urllib
import json

class util_helper():

    def initCurl(self):

        c = pycurl.Curl()
        c.setopt(pycurl.COOKIEFILE, "cookie_file_name")  # 把cookie保存在该文件中
        c.setopt(pycurl.COOKIEJAR, "cookie_file_name")
        c.setopt(pycurl.FOLLOWLOCATION, 1)  # 允许跟踪来源
        c.setopt(pycurl.MAXREDIRS, 5)
        # 设置代理 如果有需要请去掉注释，并设置合适的参数
        # c.setopt(pycurl.PROXY, ‘http://11.11.11.11:8080′)
        # c.setopt(pycurl.PROXYUSERPWD, ‘aaa:aaa’)
        return c

    def curl_get(self,url):
        curl = self.initCurl()
        head = ['Accept:*/*',
                'User-Agent:Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.97 Safari/537.11']
        buf = io.BytesIO()
        curl.setopt(pycurl.WRITEFUNCTION, buf.write)
        curl.setopt(pycurl.URL, url)
        curl.setopt(pycurl.HTTPHEADER,  head)
        curl.perform()
        the_page = buf.getvalue()
        buf.close()
        return the_page
