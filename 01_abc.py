# -*- coding: utf-8 -*-
'''
@author: heyongkang
@file: 01_abc.py
@time: 2019-02-05 11:12
@desc:a+b+c=1000,a^2+b^2=c^2,abc为自然数，求a，b，c可能组合
'''
import time

start_time = time.time()
"""方法一"""
'''
for a in range(0, 1001):
    for b in range(0, 1001):
        for c in range(0, 1001):
            if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
                print("a,b,c:%d,%d,%d" % (a, b, c))
'''
"""方法二"""
'''

for a in range(0, 1001):
    for b in range(0, 1001):
        c = 1000-a-b
        if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
            print("a,b,c:%d,%d,%d" % (a, b, c))
'''
end_time = time.time()
print("time:%d" % (end_time - start_time))
print("complete")
