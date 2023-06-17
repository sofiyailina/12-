from random import *
'''
s = list('1' * 8 + '2' * 8)
shuffle(s)
s = '0' + ''.join(s) + '0'
'''

min4 = 10**10
for _ in range(10000):
    for n in range(8, 20):
        s = list('1' * 8 + '2' * 8)
        shuffle(s)
        s = '0' + ''.join(s) + '0'
        while '00' not in s:
            if '011' in s:
                s = s.replace('011', '101', 1)
            else:
                s = s.replace('01', '40', 1)
                s = s.replace('02', '20', 1)
                s = s.replace('0220', '1401', 1)
        if s.count('1') == 6 and s.count('2') == p:
            min4 = min(min4, s.count('4'))
print(min4)            