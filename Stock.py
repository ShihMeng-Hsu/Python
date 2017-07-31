# -*- coding: utf-8 -*-
import time
import collections
import requests
from bs4 import BeautifulSoup

headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
Stock = {2330}
Title = [u'買進  ', u'賣出  ', u'成交價', u'漲跌  ']

def HtmlGet():
	Data = requests.get('https://tw.stock.yahoo.com/q/ts?s=2330', headers = headers)
	#
	# response status code 200 = succcess
	#
	if Data.status_code == 200:
		print 'Get Method Successful'
	else:
		print 'Get Method Failed. Status code = ', Data.status_code
		exit()
	return Data

def DataBs4(Data):
	Soup = BeautifulSoup(Data, "html.parser")
	return Soup

def GetCurrentDate():
	localtime = time.asctime(time.localtime(time.time()))
	return localtime

def main():
	while(1):
		# use Get method to get data by send API
		Context = HtmlGet()

		# use beautifulsoup to clean up the Context
		Soup = DataBs4(Context.text)

		# To get the curren Time/Date
		localtime = GetCurrentDate()
		print u'時間   : ', localtime

		# print title and price
		index = 0
		for i in Title:
			print i,': ', Soup.select(".high")[index].text
			index = index+1

		# wait 5 second
		time.sleep(5)

if __name__ == '__main__':
	main()