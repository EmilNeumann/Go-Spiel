'''
Created on 14.06.2015

@author: Emil
'''
import Tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit',
            command=self.quit)
        self.quitButton.grid()
        self.sc = tk.Scale(self)
        self.sc.grid()

app = Application()
app.master.title('Sample application')
app.mainloop()