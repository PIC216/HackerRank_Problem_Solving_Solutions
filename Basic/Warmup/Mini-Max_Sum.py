#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # takes an array of length 5 and prints the maximum and minimum sum of 4 values
    arr.sort()
    minsum = sum(arr[0:-1])
    maxsum = sum(arr[1:])
    print(f"{minsum} {maxsum}")

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
