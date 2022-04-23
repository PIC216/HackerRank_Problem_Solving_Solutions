#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    """
    parameters:
    x: position of cat A
    y: position of cat B
    z: position of mouse C
    function returns either the cat that catches the mouse 
    or the mouse when the cats reach the mouse at the same time and therefore fight eachother, letting the mouse get away
    """
    a_dist = abs(x-z)
    b_dist = abs(y-z)
    if a_dist == b_dist:
        return "Mouse C"
    if a_dist < b_dist:
        return "Cat A"
    elif a_dist > b_dist:
        return "Cat B"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()
