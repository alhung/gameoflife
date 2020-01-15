
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Game of Life
This program is an implementation of Conway's game of life.
The purpose of the game is to calculate the next state/generation
of a multidimensional grid given an initial state/generation of the grid

This implementation resembles a forecasting/prediction model

Assumptions for Implementation:
- Dealing with 2D grids
- Calculating only its next generation?
- No live cell off the edges (does this mean edge cells are blank?)

"""

import numpy as np
#import pickle as pk

# get # rows
def rows():
    numRow = input("Type number of rows (in digits): ")
    numRow_int = int(numRow)
    return numRow_int

# get # columns
def columns():
    numCol = input("Type number of columns (in digits): ")
    numCol_int = int(numCol)
    return numCol_int

# create initial random grid sized by user
def random_grid(x,y):
    randomgrid = np.random.randint(2, size=(x,y))
    print ("You elected to create a {} x {} grid".format(x, y))
    print (randomgrid)
    return randomgrid

# create random first generation seed file with initial state
#def seed(grid,x,y):
#    filename = "seeding"
#    with open(filename, "w") as f:
#        f.write(grid)
#        np.save(f, grid)
#        pk.dump(grid,f)
#    print ("\n2) Grid file was created, please open it and update any desired 0 to 1")
#    input ("\nPress enter after the Grid File has been updated and saved")
#    print("\nBelow is your initial state")
#    with open(filename, "r") as f:
#        values = f.read()
#        print(values)
#        return values

# ID Moore location - identify corner, noncorner edge, or central
def mooresq(first):

#    x = 0
#    y = 0
#    c = np.array(x,y)

#    for r in first:
#        for c in first:

    # setup cartesian
#    x = np.linspace(-1,1,3)
#    y = np.linspace(-1,1,3)
#    xx,yy = np.meshgrid(x,y)
#    print (xx)
#    print (yy)

    # count num datapoints as neighbors available

#    x = np.array([-1, 0, 1]);
#    y = np.array([-1, 0, 1]);
#    coordinates = np.array(x, y)
#    print (coordinates)


#    for i in np.nditer(first):
#        num = first.index(i)

def main():
    print ("\nWelcome to Conway's Game of Life\n") 
    print ("\nPlease follow below instructions to create your desired initial state\n")
    print ("Select Random Grid Size:")
    x = rows()
    y = columns()
    first = random_grid(x,y)
    next = mooresq(first)

#if  __name__ =='__main__':
    #main(sys.argv)

main()
