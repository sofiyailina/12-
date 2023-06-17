from random import *
min4 = 10**10
for _ in range(100000):
    for n in range(1, 20):
        s = list('1' * n + '2' * n)
        shuffle(s)
        s = '0' + ''.join(s) + '0'
        while '00' not in s:
            if '011' in s:
                s = s.replace('011', '101')
            else:
                s = s.replace('01', '40', 1)
                s = s.replace('02', '20', 1)
                s = s.replace('0222', '1401', 1)
        if s.count('1') == 8 and s.count('2') == 13:
            min4 = min(min4, s.count('4'))
print(min4)

