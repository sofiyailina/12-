from random import*
min4 = 10**10
for _ in range(10000):
    for n in range(8, 20):
        s = list('1' * n + '2' * n)
        shuffle(s)
        s = '0' + ''.join(s) + '0'
        while '00' not in s:
                s = s.replace('02', '101', 1)
                s = s.replace('11', '2', 1)
                s = s.replace('12', '21', 1)
                s = s.replace('010', '00', 1)
       # if s.count('1') == 6 and s.count('2') == 9:
         #   min4 = min(min4, s.count('4'))
print(min4)
