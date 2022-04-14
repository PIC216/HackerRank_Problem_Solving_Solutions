#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    original_alphabet = [x for x in "abcdefghijklmnopqrstuvwxyz"]
    new_alphabet = [x for x in "abcdefghijklmnopqrstuvwxyz"]
    for i in range(k):
        x = new_alphabet.pop(0)
        new_alphabet.append(x)
    lower = s.lower()
    new_text = ""
    for i in range(len(lower)):
        if not lower[i].isalpha():
            new_text += lower[i]
        else:
            index = original_alphabet.index(lower[i])
            new_letter = new_alphabet[index]
            if s[i].isupper():
                new_letter = new_letter.upper()
            new_text += new_letter
    return new_text

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
