class Rectangle:
    idx = 0
    xTopLeft = 0
    yTopLeft = 0
    xBottomRight = 0
    yBottomRight = 0

    def __init__(self, string):
        self.idx = int(string[1 : string.find("@") -1])
        self.xTopLeft = int(string[string.find("@ ") + 2 : string.find(",")])
        self.yTopLeft = int(string[string.find(",") + 1 : string.find(":")])
        width = int(string[string.find(": ") + 2 : string.find("x")])
        height = int(string[string.find("x") + 1 :])
        self.xBottomRight = self.xTopLeft + width
        self.yBottomRight = self.yTopLeft + height

def x_axis_overlap(rectA, rectB):
    return rectA.xTopLeft <= rectB.xTopLeft and rectA.xBottomRight >= rectB.xTopLeft

def y_axis_overlap(rectA, rectB):
    return rectA.yTopLeft <= rectB.yTopLeft and rectA.yBottomRight >= rectB.yTopLeft

def is_overlap(rectA, rectB):
    x = x_axis_overlap(rectA, rectB) or x_axis_overlap(rectB, rectA)
    y = y_axis_overlap(rectA, rectB) or y_axis_overlap(rectB, rectA)
    return x and y

inputs = open("day3/input").read().splitlines()
rectangles = map(Rectangle, inputs)

for rectA in rectangles:
    collisions = 0
    for rectB in rectangles:
        if rectA != rectB and is_overlap(rectA, rectB):
            collisions += 1
        
        if collisions > 0:
            break
    
    if collisions == 0:
        print "Done! " + str(rectA.idx)