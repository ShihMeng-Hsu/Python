# -*- coding: utf-8 -*-
from Tkinter import *

class Application(object, Frame):
    """docstring for Application"""

    def StockPage(self, Date, Infomations):

        self.TIME = Label(self)
        self.TIME["text"] = "時間  : " + Date
        self.TIME["fg"] = "black"
        self.TIME.pack({"side": "top"})

        self.BUYIN = Label(self)
        self.BUYIN["text"] = u"買進  : " + Infomations[0]
        self.BUYIN["fg"] = "black"
        self.BUYIN.pack({"side": "top"})

        self.SOLDOUT = Label(self)
        self.SOLDOUT["text"] = u"賣出  :" + Infomations[1]
        self.SOLDOUT["fg"] = "black"
        self.SOLDOUT.pack({"side": "top"})

        self.FINAL_PRICE = Label(self)
        self.FINAL_PRICE["text"] = u"成交價  : " + Infomations[2]
        self.FINAL_PRICE["fg"] = "black"
        self.FINAL_PRICE.pack({"side": "top"})

        self.DELTA = Label(self)
        self.DELTA["text"] = u"漲跌  : " + Infomations[3]
        self.DELTA["fg"] = "black"
        self.DELTA.pack({"side": "top"})

    def Search(self):
        self.arg = self.INPUT.get()
        print self.arg
        self.BuildWindow()
        self.LABEL.destroy()
        self.INPUT.destroy()
        self.SEARCH.destroy()
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