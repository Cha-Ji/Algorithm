class Solution:
    def numsSameConsecDiff(self, N: int, K: int):
        result = []
        if N == 1:
            return [0,1,2,3,4,5,6,7,8,9]
        def createElement(preElement, N, total):
            if N == 0:
                result.append(total)
                return

            digit = pow(10, N - 1)  # 자릿수
            # 자릿수를 낮춰가며 올 수 있는 숫자를 추가시킨다.
            if N == 1 and preElement == 0:
                result.append(total)
                return

            if preElement - K >= 0:
                nextElement = preElement - K
                createElement(nextElement, N - 1, total + digit * preElement)

            if preElement + K < 10:
                nextElement = preElement + K
                createElement(nextElement, N - 1, total + digit * preElement)

        # 양 옆에 어떤 숫자가 와도 조건을 만족할 수 없는 숫자 배제
        element = []
        for i in range(1, 10):
            if i+K >= 10 and i-K < 0:
                continue
            else:
                element.append(i)

        for i in element:
            createElement(i, N, 0)
        return sorted(list(set(result)))





a = Solution()
print(a.numsSameConsecDiff(2,1))
