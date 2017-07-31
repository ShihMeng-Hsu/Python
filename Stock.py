# -*- coding: utf-8 -*-
import time
#My Parser module
import Parser.StockParser
#My GUI module
import GUI.GUI

StockHtml = 'https://tw.stock.yahoo.com/q/ts?s='
#headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
#Stock = {2330}
StockData = [u'買進  ', u'賣出  ', u'成交價', u'漲跌  ']

def main():

	root = GUI.GUI.Tk()
	window = GUI.GUI.Application(root, 'Stock')

	window.mainloop()

	url = Parser.StockParser.HtmlParser(StockHtml + window.arg)
	
	# use Get method to get data by send API
	Context = url.HtmlGet()

	# use beautifulsoup to clean up the Context
	Soup = url.DataBs4(Context.text)
	for index in range(4):
#		if Soup.select(".low")[index]:
#			StockData[index] = Soup.select(".low")[index].text
#		elif Soup.select(".high"):
#			StockData[index] = Soup.select(".high")[index].text

	# To get the curren Time/Date
	localtime = url.GetCurrentDate()

	# Input data and show on application
	window.StockPage(localtime, StockData)

	window.mainloop()


#		# wait 5 second
#		time.sleep(5)

if __name__ == '__main__':
	main()