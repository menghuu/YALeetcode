#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 m <m@meng.hu>
#
# Distributed under terms of the MIT license.

"""

"""
class Solution:

    def using_pre_post_bfs(self, beginWord, endWord, wordList):
        from collections import defaultdict, deque

        wordList = set(wordList)
        if endWord not in wordList:
            return []

        wordList.add(beginWord)

        WHITE, GRAY, BLACK = 0, 1, 2
        begin_colors = {k: WHITE for k in wordList}
        end_colors = {k: WHITE for k in wordList}
        begin_colors[beginWord] = GRAY
        end_colors[endWord] = GRAY

        begin_paths = defaultdict(list)
        end_paths = defaultdict(list)
        begin_paths[beginWord].append([beginWord])
        end_paths[endWord].append([endWord])

        begin_level = deque()
        begin_level.append(beginWord)
        end_level = deque()
        end_level.append(endWord)

        pattern_vs_strs = defaultdict(set)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i + 1:]
                pattern_vs_strs[pattern].add(word)

        ans = []

        def bfs(level, total_paths, colors, other_total_paths, begin=True):
            l = len(level)
            for i in range(l):
                node = level[i]
                if colors[node] == BLACK:
                    continue

                for j in range(len(node)):
                    pattern = node[:j] + '*' + node[j + 1:]
                    for n in pattern_vs_strs[pattern]:
                        if n == node or colors[n] == BLACK or colors[n] == GRAY:
                            continue

                        for path in total_paths[node]:
                            path = path[:]
                            path.append(n)
                            total_paths[n].append(path)
                            if other_total_paths[n]:
                                for path2 in other_total_paths[n]:
                                    path = total_paths[n][-1][:]
                                    path2 = path2[:]
                                    if begin:
                                        path2 = path2[::-1][1:]
                                        path.extend(path2)
                                        ans.append(path[:])
                                    else:
                                        path = path[::-1][1:]
                                        path2.extend(path)
                                        ans.append(path2[:])

                            if n not in level:
                                level.append(n)
            for i in range(l):
                node = level.popleft()
                colors[node] = BLACK

            for i in range(len(level)):
                node = level[i]
                colors[node] = GRAY

        while begin_level and end_level:
            bfs(begin_level, begin_paths, begin_colors, end_paths, begin=True)
            if ans:
                return ans
            bfs(end_level, end_paths, end_colors, begin_paths, begin=False)
            if ans:
                return ans
        return ans

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        from collections import deque, defaultdict

        wordList = set(wordList)

        if endWord not in wordList:
            return []

        wordList.add(beginWord)

        pattern_vs_strs = defaultdict(set)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i + 1:]
                pattern_vs_strs[pattern].add(word)

        begin_paths = defaultdict(list)
        end_paths = defaultdict(list)

        begin_level = deque()
        end_level = deque()

        WHITE, GRAY, BLACK = 0, 1, 2
        begin_colors = {k: WHITE for k in wordList}
        end_colors = {k: WHITE for k in wordList}
        begin_colors[beginWord] = GRAY

        begin_level.append(beginWord)
        end_level.append(endWord)

        begin_paths[beginWord] = [[beginWord]]
        end_paths[endWord] = [[endWord]]

        ans = []

        def bfs(level, total_paths: dict, colors):
            l = len(level)
            for i in range(l):
                node = level[i]
                if node == endWord:
                    ans.extend([path[:] for path in total_paths[node]])
                    continue
                if colors[node] == BLACK:
                    continue
                for j in range(len(node)):
                    pattern = node[:j] + '*' + node[j + 1:]
                    for n in pattern_vs_strs[pattern]:
                        if n == node or colors[n] == BLACK or colors[n] == GRAY:
                            continue
                        for path in total_paths[node]:
                            path = path[:]
                            path.append(n)
                            total_paths[n].append(path)
                        if n not in level:
                            level.append(n)

            for i in range(l):
                node = level.popleft()
                colors[node] = BLACK

            for i in range(len(level)):
                node = level[i]
                colors[node] = GRAY

        while begin_level:
            bfs(begin_level, begin_paths, begin_colors)

        return ans
