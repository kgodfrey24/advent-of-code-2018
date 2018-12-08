# returns True if coords are inside the rectangle
def coords_in_rectangle(coordx, coordy, rectx, recty, rectwidth, rectheight):
    xconditions = coordx >= rectx and coordx < rectx + rectwidth 
    yconditions = coordy >= recty and coordy < recty + rectheight
    return xconditions and yconditions

with open("day3/input") as f:
    input = f.readlines()

rectangles = []

for string in input: 
    rectx = int(string[string.find("@ ") + 2 : string.find(",")])
    recty = int(string[string.find(",") + 1 : string.find(":")])
    width = int(string[string.find(": ") + 2 : string.find("x")])
    height = int(string[string.find("x") + 1 :])
    rectangles.append([rectx, recty, width, height])

total_claims_greater_than_two = 0

for xcoord in range(0, 1000):
    print xcoord
    for ycoord in range(0, 1000):
        claims = 0

        for rect in rectangles:
            rectx = rect[0]
            recty = rect[1]
            width = rect[2]
            height = rect[3]

            if coords_in_rectangle(xcoord, ycoord, rectx, recty, width, height):
                claims += 1

        if claims >= 2: 
            total_claims_greater_than_two += 1


print total_claims_greater_than_two