import turtle

# the distance we want the pointer to travel each time
DIST = 75


for x in range(0,4):
    print "x", x
    for y in range(1,9):
        print "y", y
        # turn the pointer 90 degrees to the right
        turtle.right(45)
        # advance according to set distance
        turtle.forward(DIST)
    # add to set distance
    DIST += 20