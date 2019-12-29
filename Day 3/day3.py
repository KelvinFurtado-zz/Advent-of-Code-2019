#Part 1
"""

Opening the front panel reveals a jumble of wires. Specifically, two wires are connected to a central port and extend outward on a grid. 
You trace the path each wire takes as it leaves the central port, one wire per line of text (your puzzle input).

The wires twist and turn, but the two wires occasionally cross paths. 
To fix the circuit, you need to find the intersection point closest to the central port. 
Because the wires are on a grid, use the Manhattan distance for this measurement. 
While the wires do technically cross right at the central port where they both start, 
this point does not count, nor does a wire count as crossing with itself.
Here are a few more examples:

R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83 = distance 159

R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = distance 135

What is the Manhattan distance from the central port to the closest intersection?
"""

def main():
    fileinput = input("Insert full path of input file (Ex: c:/Documents/Advent/Day3/inputfile.txt):")
    f = open(fileinput, "r")
    lst = f.readlines()
    lst = formatinput(lst)
    part1 = abssum(list(filtercolisions(list(setpath(lst)))))
    print("Part 1: ", part1)
    part2 = abssumcol(list(pathcolisions(list(setpath(lst)))))
    print("Part 2:", part2)

def pathcolisions(lst):
    colisions = list(filtercolisions(lst))
    pathcol = []
    for x in colisions:
        for y in lst:
            path = []
            for z in y:
                if z != x:
                    path.append(z)
                else:
                    path.append(z)
                    break
            pathcol.append(path)
             

    return pathcol
                
def abssum(lst):
    smallest = abs(lst[0][0]) + abs(lst[0][1])
    for x in lst:
        if abs(x[0]) + abs(x[1]) < smallest:
            smallest = abs(x[0]) + abs(x[1])
    return smallest

def abssumcol(lst):
    smallest = len(list(lst[0])) + len(list(lst[1]))
    for x in range(len(lst)):
        if x % 2 == 0:
            if len(list(lst[x])) + len(list(lst[x+1])) < smallest:
                smallest = len(list(lst[x])) + len(list(lst[x+1]))

    return smallest


def filtercolisions(lsttest2):
    filterlist = []
    for x in lsttest2[0]:
        if x in lsttest2[1]:
            filterlist.append(x)
    return filterlist

def formatinput(lst):
    lst2 = []
    for x in lst:
        lst2.append(list(x.strip('\n').split(',')))
    return lst2

def setpath(lst):
    pathlist = []
    for x in lst:
        center = (0,0)
        points = []
        for y in x:
            if y[0] == "R":
                for i in range(int(y[1:])):
                    center = (center[0] + 1, center[1])
                    points.append(center)
            elif y[0] == "L":
                for i in range(int(y[1:])):
                    center = (center[0] - 1, center[1])
                    points.append(center)
            elif y[0] == "U":
                for i in range(int(y[1:])):
                    center = (center[0], center[1] + 1)
                    points.append(center)
            elif y[0] == "D":
                for i in range(int(y[1:])):
                    center = (center[0], center[1] - 1)
                    points.append(center)
            else:
                raise Exception("Invalid direction!!!!!!!!")
        pathlist.append(list(points))
    return pathlist





main()