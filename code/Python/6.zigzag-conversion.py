class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        res = ""
        n = len(s)
        flag = [0 for i in range(n)]
        p = [numRows*2-2, 0]
        for i in range(numRows):
            index = i
            x = 0
            while index < n:
                if flag[index] == 0:
                    res += s[index]
                    flag[index] = 1
                index += p[x % 2]
                x += 1
            p[0] -= 2
            p[1] += 2
        return res
