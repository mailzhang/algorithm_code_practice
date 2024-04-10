class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        _len = len(s)
        if _len == 1:
            return s
        for i in range(_len // 2):
            t = s[i]
            _e = _len - i - 1
            s[i] = s[_e]
            s[_e] = t

        return s


if __name__ == '__main__':
    s = ["h", "e", "l", "l", "o"]
    r = Solution().reverseString(s)
    print(r)
