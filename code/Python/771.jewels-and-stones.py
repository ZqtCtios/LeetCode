class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewelSUm = 0
        for c in S:
            if c in J:
                jewelSUm += 1
        return jewelSUm
