#Part 1
"""
An Intcode program is a list of integers separated by commas (like 1,0,0,3,99). 
To run one, start by looking at the first integer (called position 0). Here, you will find an opcode - either 1, 2, or 99.
The opcode indicates what to do; for example, 99 means that the program is finished and should immediately halt. 
Encountering an unknown opcode means something went wrong.

Opcode 1 adds together numbers read from two positions and stores the result in a third position. 
The three integers immediately after the opcode tell you these three positions -
the first two indicate the positions from which you should read the input values, 
and the third indicates the position at which the output should be stored.

For example, if your Intcode computer encounters 1,10,20,30, it should read the values at positions 10 and 20, add those values,
and then overwrite the value at position 30 with their sum.

Opcode 2 works exactly like opcode 1, except it multiplies the two inputs instead of adding them. 
Again, the three integers after the opcode indicate where the inputs and outputs are, not their values.

Once you're done processing an opcode, move to the next one by stepping forward 4 positions.


Once you have a working computer, the first step is to restore the gravity assist program (your puzzle input) 
to the "1202 program alarm" state it had just before the last computer caught fire. 
To do this, before running the program, replace position 1 with the value 12 and replace position 2 with the value 2. 
What value is left at position 0 after the program halts?
"""


def main():
    fileinput = input("Insert full path of input file (Ex: c:/Documents/Advent/Day2/inputfile.txt): ")
    f = open(fileinput, "r")
    lst = f.readline().split(",")
    lst = [int(i) for i in lst]
    lst2 = list(lst) 
    print("Position 0 is: ", opcode(lst,12,2))
    noun, verb = opcode2(lst2)
    print("Part 2: (100*noun) + verb =",(100*noun) + verb)
    f.close()

def opcode(lst,l1, l2):
    lst[1] = l1
    lst[2] = l2
    for x in range(0,len(lst),4):
        a = lst[x+1]
        b = lst[x+2]
        c = lst[x+3]
        if lst[x] == 1:
            lst[c] = lst[a] + lst[b]
        elif lst[x] == 2:
            lst[c] = lst[a] * lst[b]
        elif lst[x] == 99:
            return lst[0]
        else:
            raise Exception("A wild different OPcode appears!!!")

def opcode2(lst2):
    for i in range(100):
        for j in range(100):
            copylist = lst2.copy()
            if opcode(copylist, i, j) == 19690720:
                return int(i),int(j) 



main()
