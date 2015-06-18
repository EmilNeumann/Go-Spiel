from Tkinter import *

class mainGUI():
    
    def __init__(self, master):
        
        frame = Frame(master, width=500, height=500)
        frame.pack()
        
        self.parent = master
        self.parent.title("Go")
        
        self.spielbrett = Canvas(frame, bg="white")
        self.draw()

    def draw(self):
        i = 0
        while i < 19:
            i = i + 1
            self.spielbrett.create_line(i*20, 20, i*20, 380)
        i = 0
        while i < 19:
            i = i + 1
            self.spielbrett.create_line(20, i*20, 380, i*20)
        
        self.spielbrett.place(x=50, y=50, width=400, height=400)

def main():
    root = Tk()
    app = mainGUI(root)
    root.mainloop()
    
if __name__ == '__main__':
    main()