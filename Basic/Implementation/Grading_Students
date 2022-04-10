#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def round_up_to_5(num):
    # takes any number and rounds it up to the next multiple of 5
    while num%5 != 0:
        num += 1
    return num

def new_grade(old_grade):
    # takes a single grade and determines the rounded grade when rounding is required
    if old_grade < 38:
        return old_grade
    if old_grade%5 < 3:
        return old_grade
    else:
        return round_up_to_5(old_grade)

def gradingStudents(grades):
    # takes a list of grades and rounds them all when rounding is required
    new_grades = []
    for grade in grades:
        newgrade = new_grade(grade)
        new_grades.append(newgrade)
    return new_grades

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
