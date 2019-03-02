# -*- coding:utf-8 -*-
'''
@author:coyote
@datetime:2019/3/2 17:45
@file: 07_queue.py
@function:队列
'''


class Queue(object):
    """队列"""

    def __init__(self):
        self.__list = []

    def enqueue(self, item):
        """队列中插入一个item元素"""
        self.__list.append(item)

    def dequeue(self):
        """从队列头部删除一个元素"""
        return self.__list.pop(0)

    def is_empty(self):
        """队列是否为空"""
        return self.__list == []

    def size(self):
        """返回队列大小"""
        return len(self.__list)


if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
