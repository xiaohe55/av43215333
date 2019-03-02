# -*- coding:utf-8 -*-
'''
@author:coyote
@datetime:2019/3/2 17:54
@file: 08_deque.py
@function:双端队列
'''


class Deque(object):
    """双端队列"""

    def __init__(self):
        self.__list = []

    def add_front(self, item):
        """队列中头部插入一个item元素"""
        self.__list.insert(0, item)

    def add_rear(self, item):
        """队列尾部插入一个item元素"""
        self.__list.append(item)

    def pop_front(self):
        """从队列头部删除一个元素"""
        return self.__list.pop(0)

    def pop_rear(self):
        """从队列尾部删除一个元素"""
        return self.__list.pop()

    def is_empty(self):
        """队列是否为空"""
        return self.__list == []

    def size(self):
        """返回队列大小"""
        return len(self.__list)


if __name__ == '__main__':
    q = Deque()
    q.add_front(1)
    q.add_front(2)
    q.add_front(3)
    q.add_front(4)
    q.add_rear(1)
    q.add_rear(2)
    q.add_rear(3)
    q.add_rear(4)

    print(q.pop_front())
    print(q.pop_rear())
    print(q.pop_front())
    print(q.pop_rear())
    print(q.pop_front())
    print(q.pop_rear())
    print(q.pop_front())
    print(q.pop_rear())
