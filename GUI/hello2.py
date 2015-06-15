'''
Created on 14.06.2015

@author: Emil
'''
from Tkinter import *
        
root = Tk()

class App:
    
    def __init__(self, root):
        
        def callback(event):
            print "clicked at", event.x, event.y
            
        frame = Frame(root, width=100, height=100, bg="red")
        frame.bind("<Button-1>", callback)
        frame.pack()
        
        self.button = Button(frame, text="Quit", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)
        
        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)

    def say_hi(self):
        print "hi there, everyone!"
        print str(self.hi_there)

app = App(root)

root.mainloop()
root.destroy()