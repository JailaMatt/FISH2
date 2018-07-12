def setup():
    size(400, 400)
    img = loadImage("undertheSea.jpg")
    image(img, 0, 0)
    fish(300, 300, 50, 20)
    fish(random(200, 330), random(100, 10), 50, 20)
    fish(random(300, 190), random(200, 80), 50, 20)
    fish(random(240, 250), random(100, 80), 50, 20)
    fish(random(200, 300), random(500, 100), 50, 20)
    
def fish(xMiddle, yMiddle, oWeight, oHeight):
    fill(random(125), random(155), random(79))
    ellipse(xMiddle+50, yMiddle+20, oWeight/2, oHeight/2)
