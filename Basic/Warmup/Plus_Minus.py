#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # takes an array and prints the proportion that are positive, negative, or zero
    length = len(arr)
    pos = 0
    neg = 0
    zero = 0
    for value in arr:
        if value == 0:
            zero += 1
        elif value < 0:
            neg += 1
        elif value > 0:
            pos += 1
    print(pos/length)
    print(neg/length)
    print(zero/length)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
