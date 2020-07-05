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
    def numberToWords(self, num: int) -> str:
        num_2_string = {
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine',
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen',
            20: 'Twenty',
            30: 'Thirty',
            40: 'Forty',
            50: 'Fifty',
            60: 'Sixty',
            70: 'Seventy',
            80: 'Eighty',
            90: 'Ninety'
        }
        def handle_one_part(one_str):
            if len(one_str) == 1:
                return num_2_string[int(one_str)]
            
            ans = ''
            if len(one_str) == 3 and one_str[-1] == '0' and one_str[-2] == '0' and one_str[-3] == '0':
                return ''

            if len(one_str) == 3 and one_str[-1] == '0' and one_str[-2] == '0':
                return num_2_string[int(one_str[0])] + ' Hundred'

            
            if 2 <= int(one_str[-2]) and one_str[-1] != '0':
                # 41
                shiwei = int(one_str[-2]) * 10
                gewei = int(one_str[-1])
                ans = num_2_string[shiwei] + ' ' + num_2_string[gewei]
            elif 0 == int(one_str[-2]):
                # 01 
                gewei = int(one_str[-1])
                ans = num_2_string[gewei]
            elif 1 <= int(one_str[-1]) <= 9 and 1 == int(one_str[-2]):
                # 11
                ans = num_2_string[int(one_str[-2:])]
            else:
                # 40
                ans = num_2_string[int(one_str[-2:])]
            
            if len(one_str) == 3 and one_str[0] != '0':
                ans = num_2_string[int(one_str[0])] + ' Hundred ' + ans

            return ans
        
        if num == 0:
            return 'Zero'

        units = ['', 'Thousand', 'Million', 'Billion']
        
        ans = []
        num_str = str(num)[::-1]
        for i in range(0, len(num_str), 3):
            one_str = num_str[i: i+3][::-1]
            one_str_return = handle_one_part(one_str)
            if one_str_return or i + 3 > len(num_str):
                ans.insert(0, units[i//3])
                ans.insert(0, one_str_return)
    
        return ' '.join(ans).strip()
