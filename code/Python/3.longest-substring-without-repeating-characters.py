"""
滑动窗口

"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        subStr = s[0]
        start = 0
        maxLength = 1
        for end in range(1, len(s)):
            x = subStr.find(s[end])
            subStr += s[end]
            if x < 0:
                if len(subStr) > maxLength:
                    maxLength = len(subStr)
            else:
                start += x+1
                subStr = s[start:end+1]
        return maxLength
