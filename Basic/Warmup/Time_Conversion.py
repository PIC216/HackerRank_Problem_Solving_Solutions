#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Converts a time from 12 hour format to 24 hour format, both input and output are strings
    time = s[0:-2]
    time_list = time.split(":")
    ampm = s[-2:]
    if ampm == "PM" and time_list[0] != "12":
        new_time = str(int(time_list[0])+12)
        time_list[0] = new_time
    elif ampm == "AM" and time_list[0] == "12":
        new_time = "00"
        time_list[0] = new_time
    new_time = ":".join(time_list)
    return new_time

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
