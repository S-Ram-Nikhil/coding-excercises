
def sort_by_name():
    """
    You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
    1: Sort based on name;
    2: Then sort based on age;
    3: Then sort by score.
    The priority is that name > age > score.

    """
    from operator import itemgetter

    l = []
    while True:
        s = input()
        if not s:
            break
        l.append(tuple(s.split(",")))

    print(sorted(l))

# sort_by_name()

def find_position():
    import math
    pos = [0,0]
    while True:
        s = input()
        if not s:
            break
        movement = s.split(" ")
        direction = movement[0]
        steps = int(movement[1])
        if direction=="UP":
            pos[0]+=steps
        elif direction=="DOWN":
            pos[0]-=steps
        elif direction=="LEFT":
            pos[1]-=steps
        elif direction=="RIGHT":
            pos[1]+=steps
        else:
            pass

    print(int(round(math.sqrt(pos[1]**2+pos[0]**2))))
# find_position()

def is_pangram(sentence):
    from string import ascii_lowercase

    sentence_set = sentence.lower()
    letters= all(letter in sentence_set for letter in ascii_lowercase)
    return letters



# print(is_pangram("qwertyuiopasdfghjklzxcvbn"))


## Random Robot name

from itertools import product
from random import shuffle
from string import ascii_uppercase as letters
# There's only 676,000 names, so just generate them all.
letter_pairs = (''.join(p) for p in product(letters, letters))
numbers = (str(i).zfill(3) for i in range(1000))
names = [l + n for l, n in product(letter_pairs, numbers)]
shuffle(names)
NAMES = iter(names)
class Robot(object):
    def __init__(self):
        self.reset()
    def reset(self):
        self.name = next(NAMES)

# a= Robot()
# print(a)


import re
def is_paired(stg):
    brackets, has_pair = re.sub(r"[^{}[\]()]", "", stg), 1
    print(brackets, has_pair)
    while has_pair:
        brackets, has_pair = re.subn(r"{}|\[]|\(\)", "", brackets)
        print(brackets, has_pair)
    return not brackets

# is_paired('{)')


def D_array(row,col):
    """
    Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
    """

    # input_str = input()
    # dimensions=[int(x) for x in input_str.split(',')]
    rowNum=row
    colNum=col
    multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
    print(multilist)
    for row in range(rowNum):
        for col in range(colNum):
            multilist[row][col]= row*col

    print(multilist)

# D_array(3,4)


def binary_divisible():
    """
    Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
    """
    value = []
    items = [x for x in input().split(',')]
    for p in items:
        intp = int(p, 2)
        print(intp)
        if not intp % 5:
            value.append(p)

    print(','.join(value))

# binary_divisible()

def count_emma(statement):
    print("Given String: ", statement)
    count= statement.count('Emma')
    print("Emma appeared ", count, "times")

# count_emma("Emma is good developer. Emma is a writer")


