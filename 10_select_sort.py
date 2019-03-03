# -*- coding:utf-8 -*-
'''
@author:coyote
@datetime:2019/3/2 20:28
@file: 10_select_sort.py
@function:选择排序
'''


def select_sort(alist):
    """选择排序"""
    n = len(alist)
    for j in range(n - 1):
        min_index = j
        for i in range(j + 1, n):
            if alist[min_index] > alist[i]:
                min_index = i
        alist[j], alist[min_index] = alist[min_index], alist[j]


if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    select_sort(li)
    print(li)
