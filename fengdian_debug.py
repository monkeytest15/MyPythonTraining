# -*- coding: utf-8 -*-

import urllib2, time, cookielib, socket,httplib
from bs4 import BeautifulSoup
from urllib2 import Request, urlopen, URLError, HTTPError
from StringIO import StringIO
import re


number = []
count =0
dianming = []
proxy = []
xingzhengqu = [1,2,3,4,5,6,7,8,9,10,13,5937,5938,5937,5939,11]
BASE_URL = 'http://www.dianping.com'
fengdian_number = []

proxy_file = file('/Users/apple/Desktop/python/ServerApiTest/webgrap/proxy.txt', 'r')
for infile_line in proxy_file.readlines():
	infile_line=infile_line.strip('\n')
	proxy.append(infile_line)
#	print proxy


try:
	opener = urllib2.build_opener(urllib2.ProxyHandler({"http":'http://180.166.50.106:8000'}))
	urllib2.install_opener( opener)
	headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}  
	req = urllib2.Request('http://www.dianping.com/shop/5266922', headers=headers)
#print webpage.read()
	webpage= urllib2.urlopen(req,timeout = 30)
	soup = BeautifulSoup(webpage.read())
	fengdian_top_div = soup.find('div', {'class':'main page-sa page-shop Fix'})
	fengdian_class= fengdian_top_div.findAll('div', {'class':'shop-name'})
	fengdian_links = [div.findAll('a') for div in fengdian_class]
	print str(fengdian_links[0][0])[-15:-4]
	fengdian_number.append(str(fengdian_links[0][0])[-15:-4])

	time.sleep(1)

except URLError, e:
	print 'time out'
	count = count+1
	
except socket.timeout, e:
	print 'socket time out'
	count = count+1
	
except httplib.BadStatusLine,e:
	print 'BadStatusLine error'	
	count = count+1
	
except AttributeError,e:
	print'no page-shop'	
	



	
	





