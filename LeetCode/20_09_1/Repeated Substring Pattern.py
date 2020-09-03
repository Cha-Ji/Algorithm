class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        length = len(s)
        for i in range(1,length//2 + 1):
            break_point = False

            # 반복을 발견한다면,
            if s[:i] == s[i:2*i] and length % i == 0:

                # 끝까지 반복시킨다.
                # i*(j+2) <= length
                for j in range(1, length//i - 1):
                    if s[i*j:i*(j+1)] != s[i*(j+1):i*(j+2)]:
                        break_point = True
                        break

                # 검증에 성공했다면 True 반환
                if not break_point:
                    return True
        return False


a = Solution()
print(a.repeatedSubstringPattern("ababba"))
