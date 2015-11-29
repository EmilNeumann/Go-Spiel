#coding: utf-8
import sys
import logging
import getpass
import dns
from optparse import OptionParser

import sleekxmpp

class EchoBot(sleekxmpp.ClientXMPP):
    
    def __init__(self, jid, password):
        super(EchoBot, self).__init__(jid, password)
        self.add_event_handler('session_start', self.start)
        self.add_event_handler('message', self.message)
    
    def start(self, event):
        self.send_presence()
        self.get_roster()
    
    def message(self, msg):
        if msg['type'] in ('normal', 'chat'):
            msg.reply("Thanks for sending:\n%s" % msg['body']).send()

if __name__=='__main__':
    '''Configure and read command-line-options'''
    optp = OptionParser()
    
    optp.add_option('-d', '--debug', help='set logging to DEBUG', action='store_const', dest='loglevel', const=logging.DEBUG, default=logging.INFO)
    optp.add_option('-j', '--jid', dest='jid', help='JID to use')
    optp.add_option('-p', '--password', dest='password', help='password to use')
    
    opts, args = optp.parse_args()
    
    if opts.jid is None:
        opts.jid = raw_input('Username: ')
    if opts.password is None:
        opts.password = getpass.getpass('Password: ')
    
    logging.basicConfig(level=opts.loglevel, format='%(levelname)-8s %(message)s')
    
    '''instantiate EchoBot'''
    xmpp = EchoBot(opts.jid, opts.password)
    xmpp.register_plugin('xep_0030')
    xmpp.register_plugin('xep_0199')#xep_0004
    
    '''connecting the Bot and listening to messages'''
    if xmpp.connect():
        xmpp.process(block=True)
    else:
        print 'Unable to connect'

'''
By passing block=True to sleekxmpp.basexmpp.BaseXMPP.process() we are running the main processing loop
in the main thread of execution. The sleekxmpp.basexmpp.BaseXMPP.process() call will not return until after SleekXMPP disconnects.
If you need to run the client in the background for another program, use block=False to spawn the processing loop in its own thread.
'''