import terminal as t
import common as c
import mirror as m
def createLevel(p:c.player, lvl:int):
    #TODO
    return None

def doGame():
    incom:bool = False
    done:bool = False
    player:c.player = c.player()
    level:c.floor = createLevel(player, 0)
    #have area and player. Now determine what to do
    while not done:
        player.chats += 1
        m.doAreaQuirks(player, level, incom)
        
        #ask for message
        comm = input("> ")
        req:t.request = t.request(comm, player.chats, incom)
        #process request
        m.process(req, player.floor_level)
        #this needs to do response, messing around, and function
doGame()