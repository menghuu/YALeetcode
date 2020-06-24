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
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        def is_num_log(log):
            index = log.index(' ')
            return log[index+1].isdigit()            

        def get_str_log_score(log):
            index = log.index(' ')
            score = log[index+1:] + log[:index]
            return score

        str_logs = []
        num_logs = []

        for log in logs:
            if is_num_log(log):
                num_logs.append(log)
            else:
                str_logs.append(log)
        
        str_logs = list(sorted(str_logs, key=get_str_log_score))

        return str_logs + num_logs
