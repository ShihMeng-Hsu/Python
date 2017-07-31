import requests
from bs4 import BeautifulSoup

headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
Stock = {2330}

def HtmlGet():
	Data = requests.get('https://tw.stock.yahoo.com/q/ts?s=2330', headers = headers)
	if Data.status_code == 200:
		print 'Get Method Successful'
	else:
		print 'Get Method Failed. Status code = ', Data.status_code


def main():
	HtmlGet()

if __name__ == '__main__':
	main()