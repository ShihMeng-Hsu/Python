# -*- coding: utf-8 -*-
import time
import requests
from bs4 import BeautifulSoup

headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
#Stock = {2330}
#Title = [u'買進  ', u'賣出  ', u'成交價', u'漲跌  ']

class HtmlParser(object):
	"""docstring for HtmlParser"""
	def HtmlGet(self):
		Data = requests.get(self.url, headers = headers)
		#
		# response status code 200 = succcess
		#
		if Data.status_code == 200:
			print 'Get Method Successful'
		else:
			print 'Get Method Failed. Status code = ', Data.status_code
			exit()
		return Data

	def DataBs4(self, Data):
		Soup = BeautifulSoup(Data, "html.parser")
		return Soup

	def GetCurrentDate(self):
		localtime = time.asctime(time.localtime(time.time()))
		return localtime

	def __init__(self, url):
		super(HtmlParser, self).__init__()
		self.url = url
		


def main():
	url = HtmlParser('https://tw.stock.yahoo.com/q/ts?s=2330')
	while(1):
		# use Get method to get data by send API
		Context = url.HtmlGet()

		# use beautifulsoup to clean up the Context
		Soup = url.DataBs4(Context.text)

		# To get the curren Time/Date
#		localtime = url.GetCurrentDate()
#		print u'時間   : ', localtime

		# print title and price
		index = 0
		for i in Title:
			print i,': ', Soup.select(".high")[index].text
			index = index+1

		# wait 5 second
		time.sleep(5)

if __name__ == '__main__':
	main()