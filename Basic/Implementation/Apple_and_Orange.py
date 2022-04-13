#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def landing(tree, distances):
    landings = []
    for distance in distances:
        landings.append(tree+distance)
    return landings

def on_house(start, end, landings):
    number = 0
    for value in landings:
        if start <= value <= end:
            number += 1
    return number
    
def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    apple_landings = landing(a, apples)
    orange_landings = landing(b, oranges)
    apples_on_house = on_house(s, t, apple_landings)
    oranges_on_house = on_house(s, t, orange_landings)
    print(apples_on_house)
    print(oranges_on_house)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
