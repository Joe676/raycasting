from wall import Wall
from ray import Ray
from particle import Particle

walls = []
render = []
vel = (0, 0)
MapH = 100
MapW = 100
SceneW = 1000
SceneH = 1000

def setup():
    size(1600, 800)
    global p
    p = Particle((SceneW/2, SceneH/2))
    global MapX
    global MapY
    MapX = 0 
    MapY = height - MapH
    
    for i in range(4):
        walls.append(Wall(random(SceneW), random(SceneH), random(SceneW), random(SceneH)))
    walls.append(Wall(0, 0, SceneW, 0))
    walls.append(Wall(0, 0, 0, SceneH))
    walls.append(Wall(SceneW, 0, SceneW, SceneH))
    walls.append(Wall(0, SceneH, SceneW, SceneH))
    
def draw():
    render = []
    rectMode(CORNERS)
    background(0)
    noStroke()
    fill(0, 200, 150)
    rect(0, height/2, width, height)
    noFill()
    render = p.look(walls)
    p.update((p.pos[0]+vel[0], p.pos[1]+vel[1]))
    
    noStroke()
    for r in render:
        fill(r[0])
        rect(r[1], r[2], r[3], r[4])
    
    rectMode(CORNER)
    fill(20, 50)
    stroke(255)
    rect(MapX, MapY, MapW, MapH)
    for wall in walls:
        wall.show()
    p.show()
    


def keyPressed():
    x = 5
    a = 5
    if(keyCode == UP):
        vel = PVector.fromAngle(radians(p.angle))
        p.update((p.pos[0]+vel.x*x, p.pos[1]+vel.y*x)) 
        print("UGH")
    if(keyCode == DOWN):
        vel = PVector.fromAngle(radians(p.angle))
        p.update((p.pos[0]+vel.x*(-x), p.pos[1]+vel.y*(-x)))
    if(keyCode == LEFT):
        avel = -5
        p.aupdate(p.angle + avel)
    if(keyCode == RIGHT):
        avel = 5
        p.aupdate(p.angle + avel)

def keyReleased():
        vel = (0, 0)
        avel = 0