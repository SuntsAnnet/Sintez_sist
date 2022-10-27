'''
Nth power rules them all!
https://www.codewars.com/kata/58aed2cafab8faca1d000e20
'''
import numpy as np
def modified_sum(a, n):

    return  sum(np.power(a,n)) - sum(a)