'''
Created on 24.07.2015

@author: Emil
'''
from Tkinter import Label

class Stein(Label):
    def __init__(self, x=0, y=0, color=0):
        
        self.color = color
        self.x = x
        self.y = y