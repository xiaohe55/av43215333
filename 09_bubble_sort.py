# -*- coding:utf-8 -*-
'''
@author:coyote
@datetime:2019/3/2 19:29
@file: 09_bubble_sort.py
@function:冒泡排序
稳定
'''


def bubble_sort(alist):
    """冒泡排序"""
    n = len(alist)
    for j in range(n - 1):
        for i in range(0, n - 1 - j):
            # 从头走到尾
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]


if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    bubble_sort(li)
    print(li)
