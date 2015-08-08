from Tkinter import *
#from classes import *

class mainGUI():
    """
    Definition des Fensters,
    in dem das Spiel ablaufen soll
    """
    def __init__(self, master):                     #Klassenkonstruktor, methode zum generieren des Fensters
        
        self.frame = Frame(master, width=500, height=600)#Festlegung der Groesse
        self.frame.pack()                                #Platzierung des Fensters auf dem Bildschirm
        self.parent = master
        self.parent.title("Go")                     #Festlegung des Namen des Fensters
        self.initializeComponents()
        
    def initializeComponents(self):
        """
        Methode, die fuer die Initialisierung der Komponenten zustaendig ist
        """
        self.fertigButton = Button(self.frame, text="Fertig")
        self.fertigButton.place(x=200, y=500, height=50, width=100)
        self.fertigButton.bind("<Button-1>", self.zug_senden)
        
        self.spielfeldstatus = [
            [0]*19, [0]*19, [0]*19, [0]*19, [0]*19,
            [0]*19, [0]*19, [0]*19, [0]*19, [0]*19,
            [0]*19, [0]*19, [0]*19, [0]*19, [0]*19,
            [0]*19, [0]*19, [0]*19, [0]*19]
        
        self.draw()                                     #Anzeigen des Spielbretts
    
    def setStone(self, event):
        """
        Methode zum setzen der Steine
        """
        x = (event.x - 10) / 20
        y = (event.y - 10) / 20
        if (0 <= x < 19) and (0 <= y < 19):
            if self.spielfeldstatus[x][y] == 0:
                self.spielfeldstatus[x][y] = 2      #setzt einen weissen Stein
        self.draw()
    
    def setBack(self, event):
        """
        mit dieser Methode kann man Steine zuruecknehmen,
        wenn man sie versehentlich gesetzt hat
        """
        x = (event.x - 10) / 20
        y = (event.y - 10) / 20
        if (0 <= x < 19) and (0 <= y < 19):
            if 1 == 1:
                self.spielfeldstatus[x][y] = 0      #loescht einen gesetzten Stein
        self.draw()
        
    def draw(self):
        """
        Methode zum Zeichnen des Spielfelds mit Steinen
        """
        self.spielbrett = Canvas(self.frame, bg="white") #Definition des Spielbretts
        self.spielbrett.bind("<Button-1>", self.setStone)
        self.spielbrett.bind("<Button-3>", self.setBack)
        i = 0
        while i < 19:                               #Schleife zum Zeichnen der senkrechten Linien
            i += 1
            self.spielbrett.create_line(i*20, 20, i*20, 381)
        i = 0
        while i < 19:                               #Schleife zum Zeichnen der waagerechten Linien
            i += 1
            self.spielbrett.create_line(20, i*20, 380, i*20)
        x = 0
        while x < 19:
            y = 0
            while y < 19:
                if self.spielfeldstatus[x][y] == 2:
                    self.spielbrett.create_oval(x*20+11, y*20+11, x*20+29, y*20+29)     #zeichnet eine leere Elipse bei weissen Steinen
                if self.spielfeldstatus[x][y] == 1:
                    pass                                                                #macht nichts, wenn ein schwarzer Stein vorhanden ist
                y += 1
            x += 1
        
        self.spielbrett.place(x=50, y=50, width=400, height=400)    #Platzierung des Spielbretts im Fenster

    def zug_senden(self, event):
        """
        Methode zum senden der Daten:
        -ob ein Stein gesetzt wurde; wenn ja,
        -wo der Stein gesetzt wurde (Koordinaten) und ggf.
        -welche Farbe der Stein hat
        """
        pass                                        #macht erst mal nichts
    
def main():
    """
    Methode, die das Programm laufen laesst
    """
    root = Tk()
    app = mainGUI(root)
    root.mainloop()
    
if __name__ == '__main__':
    
    main()
    