class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1 = version1.split(".")
        ver2 = version2.split(".")

        i = 0
        while i < min(len(ver1), len(ver2)):
            if int(ver1[i]) > int(ver2[i]):
                return 1
            if int(ver1[i]) < int(ver2[i]):

                return -1
            i += 1
        if len(ver1) > len(ver2) and int(ver1[-1]) > 0:
            return 1
        elif len(ver1) < len(ver2) and int(ver2[-1]) > 0:
            return -1
        return 0
a = Solution()
print(a.compareVersion("1.1.0","1.1"))
