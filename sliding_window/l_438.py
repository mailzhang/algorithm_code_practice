from collections import defaultdict


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        res = []

        d_len = len(p)

        left = 0
        valid = 0
        need = defaultdict(int)
        for _t in p:
            need[_t] += 1

        windows = defaultdict(int)

        for right, r_char in enumerate(s):
            windows[r_char] += 1

            if need.get(r_char, 0) == windows.get(r_char, 0):
                valid += 1

            while valid == len(need):
                if right - left + 1 == d_len:
                    res.append(left)
                l_char = s[left]
                windows[l_char] -= 1
                left += 1
                if need.get(l_char, 0) > windows.get(l_char, 0):
                    valid -= 1
        return res


if __name__ == '__main__':
    s = "cbaebabacd"
    p = "abc"
    r = Solution().findAnagrams(s, p)
    print(r)
