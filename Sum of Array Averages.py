'''
Sum of Array Averages
https://www.codewars.com/kata/56d5166ec87df55dbe000063
'''
import math
def sum_average(arr):
    average = 0
    for i in range(len(arr)):
        average += sum(arr[i])/len(arr[i])
    return math.floor(average)