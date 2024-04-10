import collections


class Solution(object):

    def plus_one(self, s, index):
        ch = list(s)
        if ch[index] == '9':
            ch[index] = '0'
        else:
            ch[index] = str(int(ch[index]) + 1)

        return ''.join(ch)

    def redu_one(self, s, index):
        ch = list(s)
        if ch[index] == '0':
            ch[index] = '9'
        else:
            ch[index] = str(int(ch[index]) - 1)

        return ''.join(ch)

    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        deadends_plus = set(deadends)
        q = collections.deque(['0000',])
        if target in q:
            return 0
        # 起始为非法
        if '0000' in deadends_plus:
            return -1

        row_ = 1
        while q:
            _len = len(q)
            for _ in range(_len):
                tem_ = q.popleft()
                for i in range(4):
                    _p = self.plus_one(tem_, i)
                    if _p not in deadends_plus:
                        q.append(_p)
                        deadends_plus.add(_p)
                    _d = self.redu_one(tem_, i)
                    if _d not in deadends_plus:
                        q.append(_d)
                        deadends_plus.add(_d)
                    if _p == target or _d == target:
                        return row_
            row_ += 1

        return -1

if __name__ == '__main__':
    # q = collections.deque(['0000', '0200', '0400'])
    # tem_ = q.popleft()
    # print(tem_)
    ch = list('0000')
    print(ch)
    for i in range(4):
        print(ch[i])

