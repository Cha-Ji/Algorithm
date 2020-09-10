# zip을 사용해 볼 것
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a, b = 0, 0
        secret, guess = list(secret), list(guess)

        # check A, del checked
        for i, j in range(len(secret)):
            if secret[i] == guess[i]:
                secret[i] = -1; guess[i] = -2
                a += 1

        # check B
        for i in guess:
            if i in secret:
                secret.remove(i)
                b += 1

        return str(a) + "A" + str(b) + "B"


a = Solution()
print(a.getHint("1807", "7810"))
