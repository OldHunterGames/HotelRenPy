init python:
    class Area(object):
        """Simple class to hold information about the area
        @param: id = Name of the Area (Must be unique).
        @param: label = Ren'Pys label bound to this area, defaults to id if not provided.
        @param: color = Color to paint this in the minimap.
        @param: teleport = matrix of ((x, y, Location.id)) we can teleport to, from this Area.
        """
        def __init__(self, id, color, label="", teleport=None):
            self.id = id
            self.label = label if label else id
            self.color = color
            
            self.teleport = teleport
            
            self.actors = set() # To be used in the future, actors that are present in this Area.
            
            areas[self.id] = self
   
    class Location(object):
        """Builds a map a size of given dimensions
        @param: id = Name of the location (Must be unique).
        @param: name = Name of the location, takes id if not specified.
        @param: main_name = Main name of the location, expects a string.
        @param: dimensions of the map as a tuple.
        @param: start = Entry (or returning) Point for the player.
        @param: pattern = Pattern of the map, expects a matrix of ((x, y, Area)).
        """
        def __init__(self, id, main_name="", name="", dimensions=(10, 10), start=(0, 0), pattern=()):
            self.id = id
            self.name = name 
            self.main_name = main_name
            self.dimensions = dimensions
            self.map = [[blocked
                               for y in xrange(self.dimensions[1])]
                               for x in xrange(self.dimensions[0])]
                               
            self.player_tile = list(start)
            
            for p in pattern:
                self.map[p[0]][p[1]] = p[2]

            self.last_coords = None
            
            locations[self.id] = self
           
        @property
        def pt(self):
            return self.map[self.player_tile[0]][self.player_tile[1]]
           
        def button_state(self, direction):
            if direction == "up":
                if self.player_tile[1] - 1 >=  0 and self.map[self.player_tile[0]][self.player_tile[1] - 1] != blocked:
                    return True
            elif direction == "down":
                if self.player_tile[1] + 1 <= self.dimensions[1] - 1 and self.map[self.player_tile[0]][self.player_tile[1] + 1] != blocked:
                    return True
            elif direction == "left":
                if self.player_tile[0] - 1 >=  0 and self.map[self.player_tile[0] - 1][self.player_tile[1]] != blocked:
                    return True
            elif direction == "right":
                if self.player_tile[0] + 1 <= self.dimensions[0] - 1 and self.map[self.player_tile[0] + 1][self.player_tile[1]] != blocked:
                    return True
            return False       
