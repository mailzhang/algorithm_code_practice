from collections import defaultdict

"""
滑动窗口

defaultdict(int) 定义一个空的 dict, value 默认是 0

注意：
 need.get(_r_char, 0) 不会在dict中生成 {_r_char:0}
 need[_r_char] 调用会生成 {_r_char:0}
 
"""

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        windows = defaultdict(int)
        need = defaultdict(int)
        tmp_len = 0
        left = 0
        right = 0
        d_start = 0
        d_length = float('inf')

        # 初始化need
        for _i in t:
            need[_i] += 1

        for _r_char in s:
            right += 1
            windows[_r_char] += 1
            if windows[_r_char] == need.get(_r_char, 0):
                tmp_len += 1

            while tmp_len == len(need):
                if right - left < d_length:
                    d_start = left
                    d_length = right - left

                _l_char = s[left]
                left += 1
                windows[_l_char] -= 1
                if need.get(_l_char, 0) > windows[_l_char]:
                    tmp_len -= 1
        # print(f"{d_start}: {d_length}")
        return "" if d_length == float("inf") else s[d_start: d_start + d_length]


if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = "ABC"
    res_ = Solution().minWindow(s, t)
    print(res_)
