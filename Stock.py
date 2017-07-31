# -*- coding: utf-8 -*-
import time
import requests
from bs4 import BeautifulSoup

headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
Stock = {2330}

Title = {u"時間":0, u"買進":0, u"賣出":0, u"成交價":0, u"漲跌":0}

def HtmlGet():
	Data = requests.get('https://tw.stock.yahoo.com/q/ts?s=2330', headers = headers)
#	if Data.status_code == 200:
#		print 'Get Method Successful'
#	else:
#		print 'Get Method Failed. Status code = ', Data.status_code
	return Data

def DataBs4(Data):
	Soup = BeautifulSoup(Data, "html.parser")
	return Soup


def main():
	# use Get method to get data by send API
	Context = HtmlGet()

	# use beautifulsoup to clean up the Context
	Soup = DataBs4(Context.text)

	localtime = time.asctime( time.localtime(time.time()) )
	print localtime
	# print title
	for i in Title:
		print i, Title[i]


	print Soup.select(".high")[0].text, Soup.select(".high")[1].text, Soup.select(".high")[2].text, Soup.select(".high")[3].text


if __name__ == '__main__':
	main()