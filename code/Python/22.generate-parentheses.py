class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        if n == 1:
            return ["()"]
        L = self.generateParenthesis(n-1)
        res = []
        for x in L[:-1]:
            if not x:
                break
            res.append("("+x+")")
            res.append("()"+x)
            res.append(x+"()")
        x = L[-1]
        res.append("("+x+")")
        res.append(x+"()")
        res.sort()
        return res


"""
递推
n=2
[
    "()()"
    "(())"
]
n=3
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]


[
    "(((())))",
    "((()()))",
    "((())())",
    "((()))()",
    "(()(()))",
    "(()()())",
    "(()())()",
    "(())(())",
    "(())()()",
    "()((()))",
    "()(()())",
    "()(())()",
    "()()(())",
    "()()()()"]
"""
