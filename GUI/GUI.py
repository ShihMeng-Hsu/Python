# -*- coding: utf-8 -*-
from Tkinter import *

class Application(object, Frame):
    """docstring for Application"""

    def Search(self):
        self.arg = self.INPUT.get()

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