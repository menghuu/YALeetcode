#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 m <m@meng.hu>
#
# Distributed under terms of the MIT license.

"""
虽然难写，但是没有什么技术含量
"""
class Solution:
    def patternMatching(self, pattern: str, value: str) -> bool:
        if len(pattern) == 0 and len(value) == 0:
            return True
        if len(pattern) == 0:
            return False
        if len(pattern) == 1 and len(value) == 1:
            return True
        if len(pattern) == 1 and len(value) == 0:
            return True

        if pattern.startswith('b'):
            return self.patternMatching(
                pattern.replace('a', 'c').replace('b', 'a').replace('c', 'b'),
                value
            )

        def get_pattern_start_index(a, pattern, value):
            for i in range(len(pattern)):
                p = pattern[i]
                if p == 'a':
                    v = value[len(a) * i: len(a) * (i + 1)]
                    if v != a:
                        return -1
                else:
                    return i
            return i + 1

        def sub_word(a, b, pattern, value):
            for p in pattern:
                if p == 'a':
                    v = value[:len(a)]
                    if v == a:
                        value = value[len(a):]
                    else:
                        return False
                else:
                    v = value[:len(b)]
                    if v == b:
                        value = value[len(b):]
                    else:
                        return False
            return value == ''

        for i in range(len(value)+1):
            a = value[:i]
            pattern_index = get_pattern_start_index(a, pattern, value)
            if pattern_index != -1:
                start_index = len(a) * pattern_index
                for j in range(start_index, len(value) + 1):
                    b = value[start_index: j]
                    if a == b :
                        continue
                    if sub_word(a, b, pattern[pattern_index:], value[start_index:]):
                        return True
        return False
