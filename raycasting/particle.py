from ray import Ray

MapH = 100
MapW = 100
SceneW = 1000
SceneH = 1000
class Particle:
    def __init__(self, pos):
        self.vel = (0, 0)
        self.pos = pos
        self.rays = []
        self.angle = 0
        self.FOV = 50
        self.q = 100
        self.lines = []
        for i in range(self.q):
            cur = map(i, 0, self.q, self.angle-self.FOV/2, self.angle+self.FOV/2)
            self.rays.append(Ray(self.pos, radians(cur)))
        self. w = width/self.q#HARDCODED WIDTH OF THE SCENE
    
    
    def show(self):
        x = map(self.pos[0], 0, SceneW, 0, MapW)
        y = map(self.pos[1], 0, SceneW, 0, MapW)
        ellipse(x, y+height-MapH, 2, 2)
        for l in self.lines:
            line(l[0], l[1], l[2], l[3])
            #line(self.pos[0], self.pos[1], self.pos[0] + ray.dir.x*5, self.pos[1] + ray.dir.y*5)
    
    def look(self, walls):
        scene = []
        self.lines = []
        i = 0
        for ray in self.rays:
            record = 500000
            rpt = None
            for wall in walls:
                pt = ray.cast(wall)
                if(pt is not None):
                    d = dist(self.pos[0], self.pos[1], pt[0], pt[1])
                    if(d < record):
                        record = d
                        rpt = pt
                    
            if(rpt is not None):
                scene.append(self.render(record, i, ray.angle))
                
                stroke(255)
                x1 = map(self.pos[0], 0, SceneW, 0, MapW)
                y1 = map(self.pos[1], 0, SceneH, 0, MapH)
                x2 = map(rpt[0], 0, SceneW, 0, MapW)
                y2 = map(rpt[1], 0, SceneH, 0, MapH)
                
                self.lines.append((x1, y1 + height - MapH, x2, y2+height-MapH))
            i+=1
        return scene
                
    def render(self, record, i, angle):
        d = record * cos(angle-radians(self.angle))
        dSq = d*d
        col = map(dSq, 0, 1000000, 255, 10)
        noStroke()
        fill(col)
        H = map(dSq, 0, 1000000, height, 50)
        if(H<0):
            H = 0
        rectMode(CENTER)
        return(col, i*self.w + self.w/2, height/2, self.w, H)
        #print(i, self.w)
    
    
    def move(self):
        self.pos = (self.pos[0] + self.vel[0], self.pos[1] + self.vel[1])
        for ray in self.rays:
            ray.pos = self.pos
            
    def update(self, pos):
        self.pos = pos#(mouseX, mouseY)
        for ray in self.rays:
            ray.pos = pos#(mouseX, mouseY)
    def aupdate(self, a):
        self.angle = a
        self.rays = []
        for i in range(self.q):
            cur = map(i, 0, self.q, self.angle-self.FOV/2, self.angle+self.FOV/2)
            self.rays.append(Ray(self.pos, radians(cur)))