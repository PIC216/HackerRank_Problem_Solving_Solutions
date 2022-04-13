#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def countforward(p):
    # counts the page turns from page 1 to page p
    if p%2==0:
        return int(p/2)
    else:
        return int((p-1)/2)
    
def countbackward(n, p):
    # counts the page turns from the back of the book (page n) to page p
    if n%2==0:
        n += 1
    if p%2==0:
        p += 1
    # print(n)
    # print(p)
    return int((n-p)/2)

def pageCount(n, p):
    # Write your code here
    if p==1 or p==n:
        return 0
    forwards = countforward(p)
    backwards = countbackward(n, p)
    if forwards <= backwards:
        return forwards
    else:
        return backwards

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
