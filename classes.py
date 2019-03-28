class Point:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.x_fixed = False
        self.y_fixed = False
        self.gdl = [(int(name)*2)-1,int(name)*2]
        
        
class Element:
    def __init__(self, name, mtype):
        self.name = name
        self.mtype = mtype
        self.incidences_i = ""
        self.incidences_f = ""
        self.elast = ""
        self.tracao = ""
        self.compress = ""
        self.area = ""
        self.comprimento = 0
        self.cos = 0
        self.sen = 0

class Load:
    def __init__(self, point):
        self.point = point
        self.intensity_x = "0"
        self.intensity_y = "0"

class Rigidez:
    def __init__(self):
        self.value = 0
        self.gdl = [-1,-1]
