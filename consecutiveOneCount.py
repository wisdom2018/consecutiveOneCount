#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/2/16 1:27 PM
# @Author: wisdom
# @File:consecutiveOne Count.py


def countConsecutiveOneNumber(number):
    maxLength = 0
    currentLength = 0
    for ele in number:
        if ele == 1:
            currentLength += 1
        else:
            currentLength = 0
        maxLength = max(currentLength, maxLength)
    return maxLength


if __name__ == '__main__':
    print('consecutive one number')
    lists = list(map(int, input().split()))
    print(lists)
    print(countConsecutiveOneNumber(lists))
