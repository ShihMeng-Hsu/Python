# -*- coding: utf-8 -*-
from Tkinter import *

Color = {u'low':"darkgreen", u'high':"red"}

class Application(object, Frame):
    """docstring for Application"""

    def StockPage(self, Infomations):

        self.TIME = Label(self)
        self.TIME["text"] = u"時間  : " + Infomations.find_all("td")[0].text
        self.TIME["fg"] = "black"
        self.TIME.pack({"side": "top"})

        self.BUYIN = Label(self)
        self.BUYIN["text"] = u"買進  : " + Infomations.find_all("td")[1].text
#        self.BUYIN["fg"] = "black"
        self.BUYIN["fg"] = Color[Infomations.find_all("td")[1].get('class')[0]]
        self.BUYIN.pack({"side": "top"})

        self.SOLDOUT = Label(self)
        self.SOLDOUT["text"] = u"賣出  :" + Infomations.find_all("td")[2].text
#        self.SOLDOUT["fg"] = "black"
        self.SOLDOUT["fg"] = Color[Infomations.find_all("td")[2].get('class')[0]]
        self.SOLDOUT.pack({"side": "top"})

        self.FINAL_PRICE = Label(self)
        self.FINAL_PRICE["text"] = u"成交價  : " + Infomations.find_all("td")[3].text
#        self.FINAL_PRICE["fg"] = "black"
        self.FINAL_PRICE["fg"] = Color[Infomations.find_all("td")[3].get('class')[0]]
        self.FINAL_PRICE.pack({"side": "top"})

        self.DELTA = Label(self)
        self.DELTA["text"] = u"漲跌  : " + Infomations.find_all("td")[4].text
#        self.DELTA["fg"] = "black"
        self.DELTA["fg"] = Color[Infomations.find_all("td")[4].get('class')[0]]
        self.DELTA.pack({"side": "top"})

        #Frame.pack_forgot()

    def Search(self, event):
        self.arg = self.INPUT.get()
        print self.arg
        self.BuildWindow()
        self.LABEL.destroy()
        self.INPUT.destroy()
        self.SEARCH.destroy()
        self.quit()
#        self.StockPage()

    def HomePageComponent (self):
        self.LABEL = Label(self)
        self.LABEL["text"] = "股票代碼 : "
        self.LABEL["fg"] = "black"
        self.LABEL.pack({"side": "left"})
        self.INPUT = Entry(self)
        self.INPUT["width"] = 10
        self.INPUT.pack({"side": "left"})

        self.SEARCH = Button(self)
        self.SEARCH["text"] = "Search"
        self.SEARCH["fg"] = "red"
        self.SEARCH["command"] = self.Search
        self.SEARCH.pack({"side": "left"})
        self.SEARCH.bind("<Enter>", self.Search)

        self.QUIT = Button(self)
        self.QUIT["text"] = "Quit"
        self.QUIT["fg"] = "red"
        self.QUIT["command"] = self.quit
        self.QUIT.pack({"side": "right"})

    def BuildWindow(self):
		self.master.title(self.arg)
    
    def __init__(self, master, arg):
        super(Application, self).__init__()
        Frame.__init__(self, master)
        self.arg = arg
        #window build
        self.pack()
        self.BuildWindow()
        self.HomePageComponent()


def main():
    root = Tk()
    window = Application(root, 'Stock')

    window.mainloop()
    root.destroy()

if __name__ == '__main__':
	main()