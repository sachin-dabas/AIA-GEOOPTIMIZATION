import Rhino.Geometry as rg

"""
INPUTS: 

OUTPUT:

"""

grid = []
for i in range(25):
    for j in range(25):
        grid.append(rg.Point3d(i,j,0))

a = grid

line = rg.Line(grid[0], grid[25])

length = line.Length

comment = 'this is a test'