#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    height = 0
    height_list = [0]
    for value in path:
        if value == "U":
            height += 1
        elif value == "D":
            height -= 1
        height_list.append(height)
    height2 = []
    for value in height_list:
        if value == 0:
            height2.append(0)
        elif value < 0:
            if len(height2)==0 or height2[-1]==0:
                height2.append("V")
        elif value > 0:
            if len(height2)==0 or height2[-1]==0:
                height2.append("M")
    valleys = height2.count("V")
    return valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
