'''
Created on 14.06.2015

@author: Emil
'''
from Tkinter import *

root = Tk()

def callback(event):
    print "clicked at", event.x, event.y

frame = Frame(root, width=100, height=100, bg="red")
frame.bind("<Button-1>", callback)
frame.pack()

root.mainloop()