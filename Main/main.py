from Tkinter import *

class mainGUI():
    
    spielbrett = Canvas(bg="white")
    
    def __init__(self, master):
        frame = Frame(master, width=500, height=500)
        frame.pack()
        self.spielbrett.place(x=50, y=50)
        self.spielbrett.size = "400x400"

root = Tk()
app = mainGUI(root)
root.mainloop(0)
#root.destroy()