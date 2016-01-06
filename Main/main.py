#coding: utf-8
from Tkinter import *
from classes import Stein

class MainGUI():
    """
    Definition des Fensters,
    in dem das Spiel ablaufen soll
    """
    def __init__(self, master):
        """
        Klassenkonstruktor; wird aufgerufen, wenn ein Objekt dieser Klasse instanziert wird
            - instanziert das Fenster
            - legt den Namen des Fensters fest
            - legt Variablen an
            - ruft die Methode initalize_components auf
        """
        self.scale = 1.0                            #: Zoomfaktor für das Spielbrett
        self.frame = Frame(master, width=500, height=600)   #: Das Fenster
        self.frame.pack()                                   #: Platzierung des Fensters auf dem Bildschirm
        self.parent = master
        self.parent.title("Go")                     #: Festlegung des Namen des Fensters
        self.stoneSet = False                      #: Boolean, hat den Wert True, wenn ein Stein gesetzt wurde
        self.stoneColor = 1                         #: Integer (Ganzzahl); hat die Werte 1 (= schwarz) und 2 (= weiß)
        self.x = -1                                 #: x-Koordinate des zuletzt gesetzen Steins
        self.y = -1                                 #: y-Koordinate des zuletzt gesetzten Steins
        self.turnList = [""]                        #: Liste der Spielzüge
        self.deletedWhiteStones = 0               #: Anzahl der geschlagenen  weißen Steine
        self.deletedBlackStones = 0               #: Anzahl der geschlagenen schwarzen Steine
        #TODO: Skalierung implementieren
        
        self.spielfeldstatus = [[None]*19 for i in range(19)]
        if not(i==18):
            print i
        
        self.initialize_components()

    def initialize_components(self):
        """
        Hier werden alle Komponenten des Fensters erzeugt:
            - eine Schaltfläche zum Beenden des Zugs
            - drei Textfelder zum Anzeigen der geschlagenen Steine
            - die Methode draw wird aufgerufen
        """
        self.readyButton = Button(self.frame, text="Fertig (aussetzen)", command=self.readyButton_click)    #: Schaltfläche zum Beenden des Zugs
        self.readyButton.place(x=300, y=500, height=50, width=100)
        
        self.label1 = Label(self.frame, width=int(15), height=1, text="geschlagene Steine:")     #: Anzeige für Text
        self.label1.place(x=100, y=480)
        
        self.label2 = Label(self.frame, width=15, height=1, text="weiße: "+str(self.deletedWhiteStones))    #: Anzeige für geschlagene weiße Steine
        self.label2.place(x=100, y=510)
        
        self.label3 = Label(self.frame, width=15, height=1, text="schwarze: "+str(self.deletedBlackStones)) #: Anzeige für geschlagene schwarze Steine
        self.label3.place(x=100, y=540)
        
        self.draw()                                     #Generieren und Anzeigen des Spielbretts

    def change_size(self, event):
        scale_x = float(self.frame.winfo_width())/500.0
        scale_y = float(self.frame.winfo_height())/600.0
        if scale_x < scale_y:
            self.scale = scale_x
        else:
            self.scale = scale_y
        self.initialize_components()

    def left_click(self, event):
        """
        Methode, die aufgerufen wird,
        wenn mit der linken Maustaste geklickt wird;
        versucht einen Stein an der angeklickten Stelle zu setzen
        """
        x = int(float(event.x - 10) / 20)
        y = int(float(event.y - 10) / 20)
        self.set_stone(x, y)
        self.readyButton = Button(self.frame, text="Fertig", command=self.readyButton_click)
        self.readyButton.place(x=300, y=500, height=50, width=100)

    def right_click(self, event):
        """
        Methode, die aufgerufen wird,
        wenn mit der rechten Maustaste geklickt wird;
        versucht, einen Stein an der angeklickten Stelle zu schlagen
        """
        x = int(float(event.x - 10) / 20)
        y = int(float(event.y - 10) / 20)
        self.del_stone(x, y)

    def double_click(self, event):
        """
        Methode, die aufgerufen wird, wenn
        doppelt mit der linken Maustaste geklickt wird;
        versucht, einen Stein an der angeklickten Stelle zurückzunehmen
        """
        x = int(float(event.x - 10) / 20)
        y = int(float(event.y - 10) / 20)
        self.set_back(x, y)
        self.readyButton = Button(self.frame, text="Fertig (aussetzen)", command=self.readyButton_click)
        self.readyButton.place(x=300, y=500, height=50, width=100)

    def readyButton_click(self):
        """
        Methode, die aufgerufen wird, wenn auf die Schaltfläche 'Fertig' geklickt wird:
            - Speichert den Spielzug
            - wechselt die Farbe, mit der der nächste Stein gesetz wird
            - ändert den Namen des Fensters
            - plaziert die Schaltfläche 'Fertig' neu (um den Text zurückzusetzen)
        """
        self.save_turn()
        self.stoneColor = (self.stoneColor%2)+1
        if(self.stoneColor == 1):
            self.parent.title("Go - schwarz am Zug")
        elif(self.stoneColor == 2):
            self.parent.title("Go - weiß am Zug")
        self.initialize_components()

    def mouse_move(self, event):
        """
        Methode, die aufgerufen wird, wenn mit
        der Maus über das Spielbrett gefahren wird;
            - ruft die Methode draw auf
            - zeichnet einen grauen Stein dort, wo sich der Mauszeiger befindet
        """
        sc = self.scale
        self.draw()
        x = int(float(event.x - 10) / 20)
        y = int(float(event.y - 10) / 20)
        if not self.stoneSet:
            if self.stoneColor == 1:
                self.canvas.create_oval(x*20+11, y*20+11, x*20+29, y*20+29, outline="#7f7f7f", fill="#7f7f7f")
            if self.stoneColor == 2:
                self.canvas.create_oval(x*20+11, y*20+11, x*20+29, y*20+29, outline="#7f7f7f", fill="#bfbfbf")

    def set_stone(self, x, y):
        """
        Methode zum Setzen der Steine:
            - überprüft, ob das angeklickte Feld noch frei ist
            - plaziert die Schaltfläche 'Fertig' neu, um den Text zu ändern
        """
        if (0 <= x < 19) and (0 <= y < 19):
            if (self.spielfeldstatus[x][y] == None):#and(not self.stoneSet)
                self.spielfeldstatus[x][y] = Stein(x, y, self.stoneColor)
                self.stoneSet = True
                self.x = x
                self.y = y
                self.initialize_components()

    def set_back(self, x, y):
        """
        mit dieser Methode kann man Steine zurücknehmen,
        wenn man sie versehentlich gesetzt hat:
            - löscht den Stein, den man zuletzt gesetzt hat
            - Schaltfläche bekommt einen neuen Text zugewiesen
        """
        if (0 <= x < 19) and (0 <= y < 19):
            if (self.spielfeldstatus[x][y] != None)and(x==self.x)and(y==self.y):      #man kann nur den zuletzt gesetzten Stein zurücknehmen
                self.spielfeldstatus[x][y] = None                                       #löscht einen gesetzten Stein
                self.stoneSet = False                                                 #man kann einen neuen Stein setzen
                self.initialize_components()

    def del_stone(self, x, y):
        """
        Methode zum Schlagen von Steinen:
            - schlägt nur Steine der anderen Farbe
            - verändert den Text der Textfelder, die die Anzahl der
              geschlagenen Steine anzeigt
            - ruft die Methode draw auf
        """
        if (0 <= x < 19) and (0 <= y < 19):
            if (self.spielfeldstatus[x][y] != None)and(self.stoneColor != self.spielfeldstatus[x][y].color):        #man kann weder leere Felder noch eigene Steine schlagen
                self.spielfeldstatus[x][y] = None                                                                   #löscht einen gesetzten Stein
                if self.stoneColor == 2:
                    self.deletedBlackStones+=1            #wenn weiß am Zug ist, werden schwarze Steine geschlagen
                elif self.stoneColor==1:
                    self.deletedWhiteStones+=1            #wenn schwarz am Zug ist, werden weiße Steine geschlagen
        self.initialize_components()

    def draw(self):
        """
        Methode zum Zeichnen des Spielfelds mit den Steinen;
            - instanziert das Spielfeld
            - verknüpft das Spielfeld mit den vier Methoden:
                - left_click
                - right_click
                - double_click
                - mouse_move
            - zeichnet das Liniengitter
            - markiert neun bestimmte Kreuzungspunkte
            - zeichnet alle Steine
        """
        sc = self.scale
        self.canvas = Canvas(self.frame, bg="white")                    #Instanzierung des Spielbretts
        self.canvas.bind("<Button-1>", self.left_click)
        self.canvas.bind("<Button-3>", self.right_click)
        self.canvas.bind("<Double-Button-1>", self.double_click)
        self.canvas.bind("<Motion>", self.mouse_move)
        i = 0
        while i < 19:                               #Schleife zum Zeichnen der senkrechten Linien
            i += 1
            self.canvas.create_line(i*20, 20, i*20, 381)
        i = 0
        while i < 19:                               #Schleife zum Zeichnen der waagerechten Linien
            i += 1
            self.canvas.create_line(20, i*20, 380.0, i*20)
        
        self.canvas.create_rectangle( 79,  79,  81,  81)    #zeichnet die 9 Markierungspunkte
        self.canvas.create_rectangle( 79, 199,  81, 201)
        self.canvas.create_rectangle( 79, 319,  81, 321)
        self.canvas.create_rectangle(199,  79, 201,  81)
        self.canvas.create_rectangle(199, 199, 201, 201)
        self.canvas.create_rectangle(199, 319, 201, 321)
        self.canvas.create_rectangle(319,  79, 321,  81)
        self.canvas.create_rectangle(319, 199, 321, 201)
        self.canvas.create_rectangle(319, 319, 321, 321)
        x = 0
        while x < 19:
            y = 0
            while y < 19:
                if self.spielfeldstatus[x][y] != None:
                    if self.spielfeldstatus[x][y].color == 2:
                        self.canvas.create_oval(x*20+11, y*20+11, x*20+29, y*20+29, fill="#ffffff")
                    if self.spielfeldstatus[x][y].color == 1:
                        self.canvas.create_oval(x*20+11, y*20+11, x*20+29, y*20+29, fill="#000000")
                y += 1
            x += 1
        
        self.canvas.place(x=50, y=50, width=400, height=400)    #platziert das Spielbrett

    def save_turn(self):
        """
        Methode zum Speichern der Daten:
            - ob ein Stein gesetzt wurde; wenn ja,
            - wo der Stein gesetzt wurde (Koordinaten) und ggf.
            - welche Farbe der Stein hat
        """
        if self.stoneSet:
            self.turnList += [str(self.x+1)+", "+str(self.y+1)+"\n"]
        else:
            farbe = ""
            if self.stoneColor == 1:
                farbe = "schwarz"
            else:
                farbe = "weiß"
            self.turnList += [farbe+" setzt aus\n"]
        self.f = open("spielverlauf.log", "w")
        self.f.writelines(self.turnList)
        self.f.close()
        self.x = -1
        self.y = -1
        self.stoneSet = False

def main():
    """
    Methode, die das Programm laufen lässt
    """
    root = Tk()             #Instanzierung eines leeren Fensters
    app = MainGUI(root)     #Instanzierung eines Programms, das die Vorlage root mit allen Änderungen in mainGUI modifiziert
    app.parent.mainloop()   #das Starten des Programms geht vom parent des Programms (root) aus

if __name__ == '__main__':
    main()