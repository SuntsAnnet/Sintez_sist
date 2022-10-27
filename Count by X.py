'''
Count by X
https://www.codewars.com/kata/5513795bd3fafb56c200049e
'''
def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    l = []
    for i in range(n+1):
        l.append(i*x)
    return l[1::]