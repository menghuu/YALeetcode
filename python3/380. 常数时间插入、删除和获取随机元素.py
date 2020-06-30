#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 m <m@meng.hu>
#
# Distributed under terms of the MIT license.

"""

"""
from random import choice
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.value_vs_index = {}
        self.values = []        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.value_vs_index:
            return False
        self.values.append(val)
        self.value_vs_index[val] = len(self.values) - 1
        return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.value_vs_index:
            return False

        index = self.value_vs_index.pop(val)
        last = self.values[-1]
        self.values[index] = last
        self.values.pop()
        if last in self.value_vs_index:
            self.value_vs_index[last] = index
        return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return choice(self.values)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
