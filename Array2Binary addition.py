'''
Array2Binary addition
https://www.codewars.com/kata/559576d984d6962f8c00003c
'''
def arr2bin(arr):
    if any(type(i) is not int for i in arr):
        return False
    return bin(sum(arr))[2:]