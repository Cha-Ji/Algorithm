class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        go_st, go_l, turn = 0, 0, 0

        for i in instructions:
            if i == "G":
                if turn == 0: go_st += 1
                if turn == 1: go_l += 1
                if turn == 2: go_st -= 1
                if turn == 3: go_l -= 1
            else:
                turn = (turn + 1) % 4 if i == "L" else (turn - 1) % 4

        return turn or (not go_st and not go_l)
a = Solution()
print(a.isRobotBounded("GG"))
