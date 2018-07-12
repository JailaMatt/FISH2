xCoordinate = 50
yCoordinate = 20
speed = 10
ySpeed = 20
fishSize = 30

def setup():
    size(400, 400)
    img = loadImage("undertheSea.jpg")
    image(img, 0, 0)
    fish(random(400), random(400), random(40, 60), random(10, 40))
    fish(random(400), random(400), random(40, 60), random(10, 40))
    fish(random(400), random(400), random(40, 60), random(10, 40))
    fish(random(400), random(400), random(40, 60), random(10, 40))
    fish(random(400), random(400), random(40, 60), random(10, 40))
    
def draw():
    global xCoordinate, speed, ySpeed, fishSize, yCoordinate
    leftTopBoundary = fishSize / 2
    rightBottomBoundary = 400 - fishSize / 2    
    if xCoordinate >= rightBottomBoundary or xCoordinate <= leftTopBoundary:
        speed = -speed
    if yCoordinate >= rightBottomBoundary or yCoordinate <= leftTopBoundary:
        ySpeed = -ySpeed
    yCoordinate += ySpeed
    xCoordinate += speed
    fill(255, 25, 100)
    fishSize( xCoordinate, yCoordinate, fishSize, fishSize)
    
def fish(xMiddle, yMiddle, oWidth, oHeight):
    fill(random(125), random(155), random(79))
    ellipse(xMiddle, yMiddle, oWidth, oHeight)
