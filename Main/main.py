from Tkinter import *
from classes import Stein

class mainGUI():
    """
    Definition des Fensters,
    in dem das Spiel ablaufen soll
    """
    def __init__(self, master):                     #Klassenkonstruktor, Methode zum generieren des Fensters
        """
        Klassenkonstruktor
        """
        self.frame = Frame(master, width=500, height=600)#Festlegung der Groesse
        self.frame.pack()                                #Platzierung des Fensters auf dem Bildschirm
        self.parent = master
        self.parent.title("Go")                     #Festlegung des Namen des Fensters
        self.steingesetzt = False                   #Variable, die erforderlich ist, um nicht mehrere Steine in einem Zug setzen zu koennen
        self.stonecolor = 1                         #legt fest, welche Farbe die gesetzten Steine haben
        self.x = -1                                 #x-Koordinate des zuletzt gesetzen Steins
        self.y = -1                                 #y-Koordinate des zuletzt gesetzten Steins
        self.zugliste = [""]                        #Spielverlauf in Form eines Text-Strings aus aneinandergereihten Koordinaten
        self.deleted_white_stones = 0               #Anzahl der geschlagenen  weissen Steine
        self.deleted_black_stones = 0               #Anzahl der geschlagenen schwarzen Steine
        self.initializeComponents()

    def initializeComponents(self):
        """
        Hier werden der Fertig-Knopf und das Gitter aus Spielfeldern erzeugt
        """
        self.fertigButton = Button(self.frame, text="Fertig")
        self.fertigButton.place(x=200, y=500, height=50, width=100)
        self.fertigButton.bind("<Button-1>", self.fertigButton_click)
        
        self.textbox_x = Text(self.frame, background="white", width=10, height=1)
        self.textbox_x.place(x=50, y=500)
        self.textbox_y = Text(self.frame, background="white", width=10, height=1)
        self.textbox_y.place(x=50, y=530)
        
        self.spielfeldstatus = [[None]*19 for i in range(19)]
        if not(i==18):
            print i
        self.draw()                                     #Generieren und Anzeigen des Spielbretts

    def setStone(self, x, y):
        """
        Methode zum setzen der Steine
        """
        if (0 <= x < 19) and (0 <= y < 19):
            if (self.spielfeldstatus[x][y] == None)and(not self.steingesetzt):
                self.spielfeldstatus[x][y] = Stein(x, y, self.stonecolor)
                self.steingesetzt = True
                self.x = x
                self.y = y
                self.draw()

    def setBack(self, x, y):
        """
        mit dieser Methode kann man Steine zuruecknehmen,
        wenn man sie versehentlich gesetzt hat
        """
        if (0 <= x < 19) and (0 <= y < 19):
            if (self.spielfeldstatus[x][y] != None)and(x == self.x)and(y==self.y):      #man kann nur den zuletzt gesetzten Stein zuruecknehmen
                self.spielfeldstatus[x][y] = None                                       #loescht einen gesetzten Stein
                self.steingesetzt = False
        self.draw()

    def draw(self):
        """
        Methode zum Zeichnen des Spielfelds mit Steinen
        """
        self.spielbrett = Canvas(self.frame, bg="white") #Definition des Spielbretts
        self.spielbrett.bind("<Button-1>", self.left_click)
        self.spielbrett.bind("<Button-3>", self.right_click)
        self.spielbrett.bind("<Double-Button-1>", self.double_click)
        self.spielbrett.bind("Enter", self.zug_speichern)
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
                if self.spielfeldstatus[x][y] != None:
                    if self.spielfeldstatus[x][y].color == 2:
                        self.spielbrett.create_oval(x*20+11, y*20+11, x*20+29, y*20+29, fill="#ffffff")     #zeichnet eine leere Elipse bei weissen Steinen
                        pass
                    if self.spielfeldstatus[x][y].color == 1:
                        self.spielbrett.create_oval(x*20+11, y*20+11, x*20+29, y*20+29, fill="#000000")
                        pass
                y += 1
            x += 1
        
        self.spielbrett.place(x=50, y=50, width=400, height=400)    #Platzierung des Spielbretts im Fenster

    def zug_speichern(self):
        """
        Methode zum senden der Daten:
        -ob ein Stein gesetzt wurde; wenn ja,
        -wo der Stein gesetzt wurde (Koordinaten) und ggf.
        -welche Farbe der Stein hat
        """
        if self.steingesetzt:
            self.zugliste += [str(self.x)+", "+str(self.y)+"\n"]
        else:
            farbe = ""
            if self.stonecolor == 1:
                farbe = "schwarz"
            else:
                farbe = "weiss"
            self.zugliste += [farbe+" setzt aus\n"]
        self.f = open("spielverlauf.txt", "w")
        self.f.writelines(self.zugliste)
        self.f.close()
        self.x = -1
        self.y = -1
        self.steingesetzt = False

    def left_click(self, event):
        """
        Methode, die aufgerufen wird,
        wenn mit der linken Maustaste geklickt wird
        """
        x = (event.x - 10) / 20
        y = (event.y - 10) / 20
        self.setStone(x, y)

    def del_stone(self, x, y):
        """
        Methode zum manuellen schlagen von Steinen
        """
        if (0 <= x < 19) and (0 <= y < 19):
            if (self.spielfeldstatus[x][y] != None)and(self.stonecolor != self.spielfeldstatus[x][y].color):        #man kann weder leere Felder noch eigene Steine schlagen
                self.spielfeldstatus[x][y] = None                                                                   #loescht einen gesetzten Stein
                if self.stonecolor == 2:
                    self.deleted_black_stones+=1            #wenn weiss am Zug ist, werden schwarze Steine geschlagen
                elif self.stonecolor==1:
                    self.deleted_white_stones+=1            #wenn schwarz am Zug ist, werden weisse Steine geschlagen
        self.draw()

    def right_click(self, event):
        """
        Methode, die aufgerufen wird,
        wenn mit der rechten Maustaste geklickt wird
        """
        x = (event.x - 10) / 20
        y = (event.y - 10) / 20
        self.del_stone(x, y)

    def double_click(self, event):
        """
        Methode, die aufgerufen wird, wenn
        doppelt mit der linken Maustaste geklickt wird
        """
        x = (event.x - 10) / 20
        y = (event.y - 10) / 20
        self.setBack(x, y)

    def fertigButton_click(self, event):
        self.zug_speichern()
        self.stonecolor = (self.stonecolor%2)+1
        if(self.stonecolor == 1):
            self.parent.title("Go - schwarz")
        elif(self.stonecolor == 2):
            self.parent.title("Go - weiss")

def main():
    """
    Methode, die das Programm laufen laesst
    """
    root = Tk()             #Instanzierung eines leeren Tkinter-Fensters
    app = mainGUI(root)     #Instanzierung eines Programms, das die Vorlage root mit allen Aenderungen in mainGUI modifiziert
    app.parent.mainloop()   #das Starten des Programms geht vom parent des Programms (root) aus

if __name__ == '__main__':
    main()