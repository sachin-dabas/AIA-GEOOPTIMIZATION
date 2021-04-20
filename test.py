import Rhino.Geometry as rg

grid = []
for i in range(50):
    for j in range(50):
        grid.append(rg.Point3d(i,j,0))

a = grid

line = rg.Line(grid[0], grid[50])

length = line.Length

comment = 'this is a test'