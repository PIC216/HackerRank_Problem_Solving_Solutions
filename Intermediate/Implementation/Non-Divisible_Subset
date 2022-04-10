#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def remainderpairs(n):
    # creates a list of pairs of numbers that sum to n, not including n/2
    pairlist = []
    for i in range(1, int((n-1)/2)+1):
        pairlist.append([i, n-i])
    return pairlist

def maxcount(pair, arr):
    # determines which value in pair is more common in arr and returns the count of this value
    x, y = pair
    count1 = arr.count(x)
    count2 = arr.count(y)
    if count1 > count2:
        return count1
    else:
        return count2

def nonDivisibleSubset(k, s):
    # takes a list s and integer k and returns the length of the longest subset of s where no 2 values sum to a multiple of k
    
    pairs = remainderpairs(k)
    
    # find the remainder of each value in s when divided by k
    remainders = []
    for value in s:
        remainders.append(value%k)
    
    # finding the max length of the subset
    subsetcount = 0
    for pair in pairs:
        subsetcount += maxcount(pair, remainders)
    if 0 in remainders:
        subsetcount += 1
    if k%2==0 and int(k/2) in remainders:
        subsetcount += 1
    return subsetcount

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
