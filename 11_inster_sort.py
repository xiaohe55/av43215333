# -*- coding:utf-8 -*-
'''
@author:coyote
@datetime:2019/3/2 20:53
@file: 11_inster_sort.py
@function:插入排序
'''


def insert_sort(alist):
    """插入排序"""
    n = len(alist)
    for j in range(1, n):
        i = j
        while i > 0:
            if alist[i] < alist[i - 1]:
                alist[i], alist[i - 1] = alist[i - 1], alist[i]
                i -= 1


if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    insert_sort(li)
    print(li)
