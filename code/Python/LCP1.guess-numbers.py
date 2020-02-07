class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
        sum = 0
        for i in range(len(guess)):
            if guess[i] == answer[i]:
                sum += 1
        return sum
