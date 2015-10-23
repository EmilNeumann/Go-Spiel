'''
Created on 24.07.2015

@author: Emil
'''
from Tkinter import Label

class Stein(Label):
    def __init__(self, x, y, color):
        
        self.color = color
        self.x = x
        self.y = y