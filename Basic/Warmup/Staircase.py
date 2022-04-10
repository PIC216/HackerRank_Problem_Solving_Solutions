#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # prints a 'staircase' of #'s of size n
    for i in range(n):
        string = "#" * (i+1)
        print(string.rjust(n))
        

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
