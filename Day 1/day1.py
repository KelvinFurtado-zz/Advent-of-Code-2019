#PART 1

"""
Specifically, to find the fuel required for a module, 
take its mass, divide by three, round down, and subtract 2.

For example:

For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
For a mass of 1969, the fuel required is 654.
For a mass of 100756, the fuel required is 33583.
What is the sum of the fuel requirements for all of the modules on your spacecraft?

"""

#PART 2
"""
A module of mass 14 requires 2 fuel. This fuel requires no further fuel (2 divided by 3 and rounded down is 0,
which would call for a negative fuel), so the total fuel required is still just 2.

At first, a module of mass 1969 requires 654 fuel. Then, this fuel requires 216 more fuel (654 / 3 - 2). 
216 then requires 70 more fuel, which requires 21 fuel, which requires 5 fuel, which requires no further fuel.
So, the total fuel required for a module of mass 1969 is 654 + 216 + 70 + 21 + 5 = 966.

The fuel required by a module of mass 100756 and its fuel is: 33583 + 11192 + 3728 + 1240 + 411 + 135 + 43 + 12 + 2 = 50346.
"""
#High Order Functions
"""
map(function, list)
EX: 
lst = [1,2,3,4,5]
def func(x):
    return x*2;
map(func, lst)

Output: [2,4,6,8,10]

reduce(function, list)
EX:
lst [1,2,3,4,5]
reduce(operator.add, lst)
Output: 1+2+3+4+5 = 15
"""
import math
import functools
import operator
def main():
    fileinput = input("Insert full path of input file (Ex: c:/Documents/Advent/Day1/inputfile.txt): ")
    f = open(fileinput,"r")
    lst = list(map(int,f.readlines()))
    print("RESULT PART 1:", calc(lst))
    print("RESULT PART 2:", main2(lst))

def calc(lst):
    results = []
    for x in lst:
        results.append(int(x/3) - 2)
    return functools.reduce(operator.add,results)

def calc2(value):
    x = int(value/3) - 2
    if x > 0:
        return x + calc2(x)
    else:
        return 0

def main2(lst):
    results2 = []
    for x in lst:
        results2.append(calc2(x))
    return functools.reduce(operator.add, results2)

main()

