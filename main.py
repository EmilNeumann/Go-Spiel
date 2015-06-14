from Tkinter import *

mainGUI = Tk()
mainGUI.geometry("480x480+400+50")

mainGrid = Canvas(mainGUI, bg="white", height=380, width=380)
mainGrid.place(x=50, y=50)

mainGUI.mainloop(0)