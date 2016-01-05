#coding: utf-8
from Tkinter import *
from classes import Stein
#from config import config_read
#from chat import *
#import logging

class MainGUI():
    """
    Definition des Fensters,
    in dem das Spiel ablaufen soll
    """
    def __init__(self, master):
        """
        Klassenkonstruktor, wird aufgerufen, wenn ein Objekt dieser Klasse instanziert wird
        """
        self.frame = Frame(master, width=500, height=600)   #: Instanzierung des Fensters, die Größe wird dabei festgelegt
        self.frame.pack()                                   #: Platzierung des Fensters auf dem Bildschirm
        self.parent = master
        self.parent.title("Go")                     #: Festlegung des Namen des Fensters
        self.stoneSet = False                      #: Variable, die erforderlich ist, um nicht mehrere Steine in einem Zug setzen zu können
        self.stoneColor = 1                         #: legt fest, welche Farbe die gesetzten Steine haben
        self.x = -1                                 #: x-Koordinate des zuletzt gesetzen Steins
        self.y = -1                                 #: y-Koordinate des zuletzt gesetzten Steins
        self.turnList = [""]                        #: Spielverlauf in Form eines Text-Strings aus aneinandergereihten Koordinaten
        self.deletedWhiteStones = 0               #: Anzahl der geschlagenen  weißen Steine
        self.deletedBlackStones = 0               #: Anzahl der geschlagenen schwarzen Steine
        self.scale = 1.0                            #: Zoomfaktor für das Spielbrett
        self.initialize_components()

    def initialize_components(self):
        """
        Hier werden alle Komponenten des Fensters erzeugt
        """
        self.readyButton = Button(self.frame, text="Fertig (aussetzen)", command=self.readyButton_click)
        self.readyButton.place(x=300, y=500, height=50, width=100)
        
        #self.anmelden = Button(self.frame, text="Anmelden", command=self.start_bot)
        #self.anmelden.place(x=500, y=550, height=20, width=100)
        #
        #self.textbox_x = Text(self.frame, background="white", width=10, height=1)
        #self.textbox_x.bind("<Return>", self.press_enter)
        #self.textbox_x.place(x=50, y=500)
        #self.textbox_y = Text(self.frame, background="white", width=10, height=1)
        #self.textbox_y.bind("<Return>", self.press_enter)
        #self.textbox_y.place(x=50, y=530)
        #
        #self.chatboxwrite = Text(self.frame, background="white", width=26, height=5)
        #self.chatboxwrite.bind("<Return>", self.send_message)
        #self.chatboxwrite.place(x=500, y=450)
        #
        #self.chatboxread = Label(self.frame, background="white", width=30, height=25)
        #self.chatboxread.place(x=500, y=50)
        
        self.label1 = Label(self.frame, width=15, height=1, text="geschlagene Steine:")
        self.label1.place(x=100, y=480)
        self.label2 = Label(self.frame, width=15, height=1, text="weiße: "+str(self.deletedWhiteStones))
        self.label2.place(x=100, y=510)
        self.label3 = Label(self.frame, width=15, height=1, text="schwarze: "+str(self.deletedBlackStones))
        self.label3.place(x=100, y=540)
        
        self.spielfeldstatus = [[None]*19 for i in range(19)]
        if not(i==18):
            print i
        self.draw()                                     #Generieren und Anzeigen des Spielbretts

    def left_click(self, event):
        """
        Methode, die aufgerufen wird,
        wenn mit der linken Maustaste geklickt wird
        """
        x = (event.x - 10) / 20
        y = (event.y - 10) / 20
        self.set_stone(x, y)

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
        self.set_back(x, y)

    def readyButton_click(self):
        """
        Methode, die aufgerufen wird, wenn auf den Fertig-Button geklickt wird.
        """
        self.save_turn()
        self.stoneColor = (self.stoneColor%2)+1
        if(self.stoneColor == 1):
            self.parent.title("Go - schwarz am Zug")
        elif(self.stoneColor == 2):
            self.parent.title("Go - weiß am Zug")
        self.readyButton = Button(self.frame, text="Fertig (aussetzen)", command=self.readyButton_click)
        self.readyButton.place(x=300, y=500, height=50, width=100)
        #self.textbox_x = Text(self.frame, background="white", width=10, height=1)
        #self.textbox_x.place(x=50, y=500)
        #self.textbox_y = Text(self.frame, background="white", width=10, height=1)
        #self.textbox_y.place(x=50, y=530)

    def mouse_move(self, event):
        """
        Methode, die aufgerufen wird, wenn mit
        der Maus über das Spielbrett gefahren wird
        """
        self.draw()
        x = (event.x-10)/20
        y = (event.y-10)/20
        if not self.stoneSet:
            if self.stoneColor == 1:
                self.canvas.create_oval(x*20+11, y*20+11, x*20+29, y*20+29, outline="#7f7f7f", fill="#7f7f7f")
            if self.stoneColor == 2:
                self.canvas.create_oval(x*20+11, y*20+11, x*20+29, y*20+29, outline="#7f7f7f", fill="#bfbfbf")

    def set_stone(self, x, y):
        """
        Methode zum setzen der Steine
        """
        if (0 <= x < 19) and (0 <= y < 19):
            if (self.spielfeldstatus[x][y] == None):#and(not self.stoneSet)
                self.spielfeldstatus[x][y] = Stein(x, y, self.stoneColor)
                self.stoneSet = True
                self.x = x
                self.y = y
                self.readyButton = Button(self.frame, text="Fertig", command=self.readyButton_click)
                self.readyButton.place(x=300, y=500, height=50, width=100)
                self.draw()

    def set_back(self, x, y):
        """
        mit dieser Methode kann man Steine zurücknehmen,
        wenn man sie versehentlich gesetzt hat
        """
        if (0 <= x < 19) and (0 <= y < 19):
            if (self.spielfeldstatus[x][y] != None)and(x==self.x)and(y==self.y):      #man kann nur den zuletzt gesetzten Stein zurücknehmen
                self.spielfeldstatus[x][y] = None                                       #löscht einen gesetzten Stein
                self.stoneSet = False                                                   #man kann einen neuen Stein setzen
                self.readyButton = Button(self.frame, text="Fertig (aussetzen)", command=self.readyButton_click)
                self.readyButton.place(x=300, y=500, height=50, width=100)
                self.draw()

    def del_stone(self, x, y):
        """
        Methode zum schlagen von Steinen
        """
        if (0 <= x < 19) and (0 <= y < 19):
            if (self.spielfeldstatus[x][y] != None)and(self.stoneColor != self.spielfeldstatus[x][y].color):        #man kann weder leere Felder noch eigene Steine schlagen
                self.spielfeldstatus[x][y] = None                                                                   #löscht einen gesetzten Stein
                if self.stoneColor == 2:
                    self.deletedBlackStones+=1            #wenn weiß am Zug ist, werden schwarze Steine geschlagen
                elif self.stoneColor==1:
                    self.deletedWhiteStones+=1            #wenn schwarz am Zug ist, werden weiße Steine geschlagen
        self.draw()
        self.label2 = Label(self.frame, width=15, height=1, text="weiße: "+str(self.deletedWhiteStones))
        self.label2.place(x=100, y=510)
        self.label3 = Label(self.frame, width=15, height=1, text="schwarze: "+str(self.deletedBlackStones))
        self.label3.place(x=100, y=540)

    def draw(self):
        """
        Methode zum Zeichnen des Spielfelds mit den Steinen
        """
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
            self.canvas.create_line(20, i*20, 380, i*20)
        
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
        
        self.canvas.place(x=50, y=50, width=400, height=400)    #Platzierung des Spielbretts im Fenster

    def save_turn(self):
        """
        Methode zum speichern der Daten:
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
    #config = config_read()      #objekt mit den daten aus go.ini
    #logging.basicConfig(level='DEBUG')
    main()