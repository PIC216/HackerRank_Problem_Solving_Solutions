#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def isalternating(arr):
    # takes a list and determines whether the values in the list are alternating
    n = len(arr)
    value1 = set([arr[i] for i in range(n) if i%2==0])
    value2 = set([arr[i] for i in range(n) if i%2==1])
    if len(value1)==1 and len(value2)==1:
        return True
    else:
        return False

def two_character_list(arr, pair):
    # takes a list and removes all values except those in the pair
    array = [x for x in arr if x in pair]
    return array
        
def alternate(s):
    # takes a list and determines the max length of a subset of the list which contains only two alternating values
    s_set = list(set(s))
    character_pairs = []
    for i in range(len(s_set)-1):
        for j in range(i+1, len(s_set)):
            character_pairs.append([s_set[i], s_set[j]])
    length = 0
    for pair in character_pairs:
        array = two_character_list(s, pair)
        if isalternating(array):
            if len(array) > length:
                length = len(array)
    return length
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
