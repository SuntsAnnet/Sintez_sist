'''
Difference between years. (Level 1)
https://www.codewars.com/kata/588f5a38ec641b411200005b
'''
def how_many_years (date1,date2):
    return abs(int(date1[0:4])-int(date2[0:4]))