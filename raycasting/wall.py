MapH = 100
MapW = 100
SceneW = 1000
SceneH = 1000
class Wall:
    
    def __init__(self, x1, y1, x2, y2):
        self.pos = (x1, y1, x2, y2)
    
    def show(self):
        stroke(255)
        x1 = map(self.pos[0], 0, SceneW, 0, MapW)
        y1 = map(self.pos[1], 0, SceneH, 0, MapH)
        x2 = map(self.pos[2], 0, SceneW, 0, MapW)
        y2 = map(self.pos[3], 0, SceneH, 0, MapH)
        line(x1, y1+height-MapH, x2, y2+height-MapH)