'''
Number of People in the Bus
https://www.codewars.com/kata/5648b12ce68d9daa6b000099
'''
import math
def number(bus_stops):
    s = 0
    for i in bus_stops:
        s += i[0]-i[1]
    return(s)