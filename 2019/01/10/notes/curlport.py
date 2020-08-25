# -*- coding:utf-8 -*-
import pycurl
c = pycurl.Curl()
c.setopt(c.URL, 'http://web.jarvisoj.com:32770/')
c.setopt(c.LOCALPORT, 51)
c.perform()
c.close()
