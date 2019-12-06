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
import math
import functools
import operator
def main():
    fileinput = input("File: ")
    f = open(fileinput,"r")
    lst = list(map(int,f.readlines()))
    print("RESULT:", calc(lst))

def calc(lst):
    results = []
    for x in lst:
        results.append(int(x/3) - 2)
    return functools.reduce(operator.add,results)




main()

