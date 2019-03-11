# -*- coding:utf-8 -*-
'''
@author:coyote
@datetime:2019/3/3 11:26
@file: 12_shell_sort.py
@function:希尔
不稳定

'''


def shell_sort(alist):
    """希尔排序"""
    n = len(alist)
    gap = n // 2
    # gap变化到0之前，插入算法执行的次数
    while gap > 0:
        # 插入算法，与普通的插入算法的区别是gap步长
        for j in range(gap, n):
            i = j
            while i > 0:
                if alist[i] < alist[i - gap]:
                    alist[i], alist[i - gap] = alist[i - gap], alist[i]
                    i -= gap
                else:
                    break
        # 缩短gap长
        gap //= 2


if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    shell_sort(li)
    print(li)
