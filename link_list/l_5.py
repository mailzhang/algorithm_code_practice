class Solution(object):

    def check(self, left_, right_, t_len, s):
        sum_len_ = 1
        _start = left_
        while left_ >= 0 and right_ < len(s) and s[left_] == s[right_]:
            if t_len > sum_len_:
                sum_len_ = t_len
                _start = left_
            t_len += 2
            left_ -= 1
            right_ += 1


        return _start, sum_len_

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1:
            return s
        _start = 0
        _len = 1
        for i, _char in enumerate(s):

            left_, sum_len_ = self.check(i, i, 1, s)
            if sum_len_ > _len:
                _start = left_
                _len = sum_len_
            left_, sum_len_ = self.check(i, i+1, 2, s)
            if sum_len_ > _len:
                _start = left_
                _len = sum_len_

        return s[_start: _start + _len]


if __name__ == '__main__':
    s = "cbbd"
    r = Solution().longestPalindrome(s)
    print(r)
