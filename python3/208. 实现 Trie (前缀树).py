#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 m <m@meng.hu>
#
# Distributed under terms of the MIT license.

"""

"""
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._dict = {}
        self._end = -1


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        _dict = self._dict
        for c in word:
            if c in _dict:
                _dict = _dict[c]
            else:
                _dict[c] = {}
                _dict = _dict[c]
        _dict[self._end] = {}


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        _dict = self._dict
        for c in word:
            if c not in _dict:
                return False
            _dict = _dict[c]

        return self._end in _dict            


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        _dict = self._dict
        for c in prefix:
            if c not in _dict:
                return False
            _dict = _dict[c]

        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
