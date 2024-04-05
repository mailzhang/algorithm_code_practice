from collections import defaultdict


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d_length = 0
        tmp_len = 0
        left = 0
        windows = defaultdict(int)

        for right, r_char in enumerate(s):
            windows[r_char] += 1

            if windows[r_char] == 1:
                tmp_len += 1
            if tmp_len > d_length:
                d_length = tmp_len

            while windows[r_char] != 1:
                l_char = s[left]
                if windows[l_char] == 1:
                    tmp_len -= 1
                windows[l_char] -= 1
                left += 1

        return d_length


if '__main__' == __name__:
    s = "aaa"
    r = Solution().lengthOfLongestSubstring(s)
    print(r)