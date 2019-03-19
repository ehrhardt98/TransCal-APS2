class Ponto:
    def __init__(self, id):
        self.id = id
        self.coord = []
        self.x_fixed = False
        self.y_fixed = False
        
        
class Element:
    def __init__(self, n_group, n_elements, mtype, ):
        self.n_group = n_group
        self.n_elements = n_elements
        self.mtype = mtype
        self.incidences = []
        self.material
        self.moduloelast
        self.res_tracao
        self.res_compress
        self.area

class Forca:
    def __init__(self, id, point, intensity, dir):
        self.id = id
        self.point = point
        self.intensity = intensity
        self.dir = dir
