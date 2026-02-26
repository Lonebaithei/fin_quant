#imports
import ibapi
from ibapi.client import EClient
from ibapi.wrapper import EWrapper

#vars

#class for interactive brokers bot
class IBBot(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)

#bot logic
class Bot:
    ib = None
    def __init__(self):
        #connect to interactive brokers
        ib = IBBot()
        ib.connect("127.0.0.1", 7497, 123)
        ib.run()

#start bot
bot = Bot()