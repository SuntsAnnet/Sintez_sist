'''
Hit Count
https://www.codewars.com/kata/57b6f850a6fdc76523001162
'''
def counter_effect(hit_count):
    t = []
    for i in list(map(int, hit_count)):
        s = []
        for k in range(0,i+1):
            s.append(k)
        t.append(s)

    return t