from Tkinter import *

class mainGUI():
    """
    Definition des Fensters,
    in dem das Spiel ablaufen soll
    """
    def __init__(self, master):                     #Klassenkonstruktor, methode zum generieren des Fensters
        
        self.frame = Frame(master, width=500, height=500)#Festlegung der Groesse
        self.frame.pack()                                #Platzierung des Fensters auf dem Bildschirm
        self.parent = master
        self.parent.title("Go")                     #Festlegung des Namen des Fensters
        self.initializeComponents()
        
    def initializeComponents(self):
        
        self.spielbrett = Canvas(self.frame, bg="white") #Definition des Spielbretts
        self.spielbrett.bind("<Button-1>", self.callback)
        self.spielfeldstatus = [[0]*19]*19              #0 = leer; 1 = schwarz; 2 = weiss;
        self.draw()                                     #Anzeigen des Spielbretts
    
    def callback(self, event):
        px = (event.x - 10) / 20
        py = (event.y - 10) / 20
        if self.spielfeldstatus[px][py] == 0:
            self.spielfeldstatus[px][py] = 1            #setzt leider alle felder mit dem y-wert auf 1, unabhängig vom x-wert
            print self.spielfeldstatus
        self.draw()

    def draw(self):
        i = 0
        while i < 19:                               #Schleife zum Zeichnen der senkrechten Linien
            i += 1
            self.spielbrett.create_line(i*20, 20, i*20, 380)
        i = 0
        while i < 19:                               #Schleife zum Zeichnen der waagerechten Linien
            i += 1
            self.spielbrett.create_line(20, i*20, 380, i*20)
        x = 0
        while x < 19:
            y = 0
            while y < 19:
                if self.spielfeldstatus[x][y] == 1:
                    self.spielbrett.create_oval(x*20+11, y*20+11, x*20+29, y*20+29)
                y += 1
            x += 1
        
        self.spielbrett.place(x=50, y=50, width=400, height=400)    #Platzierung des Spielbretts im Fenster

def main():
    root = Tk()
    app = mainGUI(root)
    root.mainloop()
    
if __name__ == '__main__':
    main()