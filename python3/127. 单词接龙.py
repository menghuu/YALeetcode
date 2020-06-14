#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 m <m@meng.hu>
#
# Distributed under terms of the MIT license.

"""
其实就是最简单的图的bfs，但是为啥做了这么久。。。。
双向bfs的时候，略微有点麻烦
还有，那两个level变量应该使用能原地改变的
"""
class Solution:
    def using_two_bfs(self, beginWord, endWord, wordList):
        from collections import defaultdict, deque
        wordList = set(wordList)
        if endWord not in wordList:
            return 0

        begin_level = deque()
        begin_level.append(beginWord)
        end_level = deque()
        end_level.append(endWord)
        begin_visited = {beginWord: 1}
        end_visited = {endWord: 1}
        pattern_vs_strs = defaultdict(set)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i + 1:]
                pattern_vs_strs[pattern].add(word)

        def bfs(level, visited, other_visited):
            l = len(level)
            for i in range(l):
                node = level.popleft()
                depth = visited[node]
                for j in range(len(node)):
                    pattern = node[:j] + '*' + node[j + 1:]
                    for n in pattern_vs_strs[pattern]:
                        if n in visited:
                            continue
                        if n in other_visited:
                            return depth + other_visited[n]
                        level.append(n)
                        visited[n] = depth + 1
            return 0

        while begin_level and end_level:
            ans = bfs(begin_level, begin_visited, end_visited)
            if ans:
                return ans
            ans = bfs(end_level, end_visited, begin_visited)
            if ans:
                return ans

        return ans


    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        return self.using_two_bfs(beginWord, endWord, wordList)
        import collections
        pattern_vs_strs = collections.defaultdict(set)

        for word in wordList:
            for i in range(len(word)):
                pattern_vs_strs[word[:i] + '*' + word[i+1:]].add(word)
        
        self.ans = float('inf')
        visited = {k: False for k in wordList}
        
        level = [beginWord]
        levels = []
        while level:
            l = len(level)
            levels.append(level[:])
            for i in range(l):
                node = level[i]
                visited[node] = True
                if node == endWord:
                    return len(levels)
                for j in range(len(node)):
                    pattern = node[:j] + '*' + node[j+1:]
                    for n in pattern_vs_strs[pattern]:
                        if not visited[n]:
                            level.append(n)
            level = level[l:]
        return 0
