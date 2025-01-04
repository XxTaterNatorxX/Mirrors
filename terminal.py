class request:
    req = ""
    reqNum = 0
    computer = False
    def __init__(self, reqs:str, reqNum:int, incomputer:bool):
        self.req = reqs
        self.reqNum = reqNum
        self.computer = incomputer
    def process(self):
        toReturn = self.req.split(" ")
        return toReturn
