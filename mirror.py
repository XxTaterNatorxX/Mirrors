import common as c
import command as com
import terminal as t
import random
def doAreaQuirks(player:c.player, level:c.area, incomputer:bool):
    return None
def process(req:t.request, flr_lvl:int):
    match(flr_lvl):
        case 0:
            #only looking for possesives here - and commands
            command = req.process()
            if((command[0].lower()) == "move" or (command[0].lower()) == "go"):
                com.doMove()
            elif((command[0].lower()) == "look" and len(command) == 2):
                com.doLook()
            elif((command[0].lower()) == "use"):
                com.doUse()
            elif((command[0].lower()) == "grab"):
                com.doGrab()
            else:
                found = False
                for i in range(len(command)):
                    if command[i].lower() == "i" or command[i].lower() == "my" or command[i].lower == "myself" or command[i].lower() == "me":
                        found = True
                        #adjust level and wack response
                        print(command[i] + "?")
                        break
                if not found:
                    print(req.req, req.reqNum)