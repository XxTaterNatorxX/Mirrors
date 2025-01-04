from enum import Enum
class direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3
class area(Enum):
    MIRROR = 0
    DOOR = 1
    COMPUTER = 2
    BED = 3
class wall:
    dir = None
    area = None
    def __init__(self,dir,area):
        self.dir = dir
        self.area = area
class room:
    north_wall = None
    south_wall = None
    east_wall = None
    west_wall = None
    def __init__(self):
        self.north_wall = None
        self.south_wall = None
        self.east_wall = None
        self.west_wall = None
class floor:
    current_room = None
    north_room = None
    south_room = None
    east_room = None
    west_room = None
    def __init__(self):
        self.current_room = None
        self.north_room = None
        self.east_room = None
        self.south_room = None
        self.west_room = None
    def matchRoom(self, f:room, nextRoom:room):
        if(room.north_wall.area == area.DOOR):
            self.north_room = nextRoom
        if(room.south_wall.area == area.DOOR):
            self.south_room = nextRoom
        if(room.east_wall.area == area.DOOR):
            self.east_room = nextRoom
        if(room.west_wall.area == area.DOOR):
            self.west_room = nextRoom
class player:
    floor_level:int = 0
    chats:int = 0
    current_room:room = None
    def __init__(self):
        self.floor_level:int = 0
        self.chats:int = 0
        self.current_room:room = None