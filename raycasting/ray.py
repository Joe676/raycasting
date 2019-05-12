class Ray:
    
    def __init__(self, pos, angle):
        self.pos = pos
        self.angle = angle
        #dir = PVector
        self.dir = PVector.fromAngle(angle)
    
    def cast(self, wall):
        #1st line, ray
        x1 = self.pos[0]
        y1 = self.pos[1]
        x2 = x1 + self.dir.x
        y2 = y1 + self.dir.y
        #2nd line, wall
        x3 = wall.pos[0]
        y3 = wall.pos[1]
        x4 = wall.pos[2]
        y4 = wall.pos[3]
        
        denominator = (x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4)
        if (denominator == 0):
            return
        
        t = ((x1 - x3)*(y3 - y4) - (y1 - y3)*(x3 - x4))/denominator
        u = -((x1 - x2)*(y1 - y3) - (y1 - y2)*(x1 - x3))/denominator
        if (t>0 and u>0 and u<1):
            return (x1 + t*(x2 - x1), y1 + t*(y2 - y1))
        else:
            return
        