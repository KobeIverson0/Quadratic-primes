#!/usr/bin/python
# coding:utf-8

from math import sqrt

def is_Prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

count = 0
res1 = 0
res2 = 0

for a in range(-1000, 1001):
    for b in range(-1000, 1001):
        if is_Prime(abs(b)):
            function = lambda x: x ** 2 + a * x + b
            judge = True
            n = 0
            while judge:
                judge = False
                number = abs(function(n))
                if is_Prime(number):
                    n += 1
                    judge = True
                else:
                    break
            if n > count:
                res1, res2 = a, b
                count = n
print count, res1, res2
