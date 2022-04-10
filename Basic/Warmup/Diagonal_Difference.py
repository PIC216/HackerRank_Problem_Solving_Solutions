#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # takes a matrix in the form of a nested list and returns the absolut difference in the diagonal sum
    length = len(arr)
    diagonal1 = 0
    for i in range(length):
        diagonal1 += arr[i][i]
        # print(diagonal1)
    diagonal2 = 0
    for j in range(length):
        diagonal2 += arr[j][length - (j+1)]
        # print(diagonal2)
    if diagonal1 >= diagonal2:
        return diagonal1-diagonal2
    else:
        return diagonal2-diagonal1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
