'''
Dictionary from two lists
https://www.codewars.com/kata/5533c2a50c4fea6832000101
'''
def createDict(keys, values):
    d = {}
    for i,v in enumerate(keys):
        if i < len(values):
            d[v] = values[i]
        else:
            d[v] = None
    return d