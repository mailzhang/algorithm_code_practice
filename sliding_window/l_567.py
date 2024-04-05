"""
滑动窗口
子串长度正好等于子串
"""
from collections import defaultdict


class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        need = defaultdict(int)
        windows = defaultdict(int)

        for s1_char in s1:
            need[s1_char] += 1

        tmp_left = 0
        tmp_right = 0

        valid = 0

        for r_char in s2:
            tmp_right += 1
            windows[r_char] += 1
            if windows.get(r_char, 0) == need.get(r_char, 0):
                valid += 1

            while valid == len(need):
                if tmp_right - tmp_left == len(s1):
                    return True

                l_char = s2[tmp_left]
                tmp_left += 1
                windows[l_char] -= 1
                if need.get(l_char, 0) > windows.get(l_char, 0):
                    valid -= 1
        return False


if '__main__' == __name__:
    s1 = "abcdxabcde"
    s2 = "abcdeabcdx"
    res = Solution().checkInclusion(s1, s2)
    print(res)
