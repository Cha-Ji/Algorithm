class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1 = [int(i) for i in version1.split(".")]
        ver2 = [int(i) for i in version2.split(".")]
        for i in range(min(len(ver1), len(ver2))):
            if ver1[i] > ver2[i]: return 1
            if ver1[i] < ver2[i]: return -1
        if set(ver1[i+1:]) - {0}:return 1
        if set(ver2[i+1:]) - {0}:return -1
        return 0

a = Solution()
print(a.compareVersion("1.1.0.0.0","1.1"))
