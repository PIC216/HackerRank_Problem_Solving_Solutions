#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # determines the minimum number of jumps it takes to cross a list of 0's avoiding the 1's, jumps can move 1 or 2 spaces
    n = len(c)
    avoid = []
    for i in range(n):
        if c[i] == 1:
            avoid.append(i)
    jumps = 0
    position = 0
    while position < n-1:
        jumps += 1
        if (position+2) not in avoid:
            position += 2
        else:
            position += 1
    return jumps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
