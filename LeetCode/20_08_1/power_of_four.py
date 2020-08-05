class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        powerList = [1]*16
        for i in range(15):
            powerList[i+1] = 4 << 2*i
        return num in powerList
