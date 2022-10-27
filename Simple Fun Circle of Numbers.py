'''
Simple Fun #2: Circle of Numbers
https://www.codewars.com/kata/58841cb52a077503c4000015
'''
def circle_of_numbers(n, fst):
    if fst<n/2:
        return fst+n/2
    else:
        return fst-n/2