#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#



def getTotalX(a, b):
    # Write your code here
    a.sort()
    b.sort()
    allnums = [i for i in range(a[-1], b[0]+1)]
    multiples = []
    factors = []
    for value in allnums:
        truth1 = 0
        for val1 in a:
            if value%val1 == 0:
                truth1 += 1
        if truth1 == len(a):
            multiples.append(value)
        truth2 = 0
        for val2 in b:
            if val2%value == 0:
                truth2 += 1
        if truth2 == len(b):
            factors.append(value)
    multiples = set(multiples)
    factors = set(factors)
    print(multiples)
    print(factors)
    answers = list(multiples&factors)
    print(answers)
    return len(answers)
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
