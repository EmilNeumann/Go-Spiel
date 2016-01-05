#coding: utf-8
'''
Created on 29.11.2015

@author: Emil
'''
import sleekxmpp
import logging

class ChatBot(sleekxmpp.ClientXMPP):
    def __init__(self, jid, password):
        super(ChatBot, self).__init__(jid, password)
        
        self.add_event_handler('session_start', self.start)
        self.add_event_handler('session_end', self.disconnect)
        
        if self.connect():
            self.process(block=False)
        else:
            print "unable to connect"
    
    def start(self, event):
        self.send_presence()
        self.roster = self.get_roster()
        print "ChatBot wurde erfolgreich gestartet"
    
    def end(self):
        #Abmelde-Botschaft an den Gegner schicken
        self.disconnect(wait=True)
    
    def select_opponent(self):
        pass
    
    def accept_invitation(self):
        pass
    
    def send_message(self):
        pass
    
    def message_handler(self):
        pass

if __name__=='__main__':
    pass