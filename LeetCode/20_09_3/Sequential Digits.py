class Solution:
    # 머리:1 길이:3 return 123
    def sortedNum(self, first_num, length):
        result = str(first_num)
        if first_num + length > 10:
            return -1
        # 문자형으로 정렬된 숫자를 뒤에 붙인다.
        for i in range(first_num+1, first_num + length):
            result += str(i)
        return int(result)

    def sequentialDigits(self, low: int, high: int):
        len_low = len(str(low))
        len_high = len(str(high))

        result = []
        # 자릿수에 대한 반복
        for i in range(len_low, len_high + 1):
            # 첫 머리는 1~9가 올 수 있다.
            for j in range(1, 10):
                this_num = self.sortedNum(j, i)
                # 범위를 만족하면 결과배열에 추가
                if low <= this_num <= high:
                    result.append(this_num)

        return result


a = Solution()
print(a.sequentialDigits(100, 3000))
