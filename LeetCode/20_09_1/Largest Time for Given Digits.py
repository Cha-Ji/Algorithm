class Solution:
    def largestTimeFromDigits(self, A:list) -> str:

        def startTwo(A):
            # result[0]
            result = '2'
            A.pop(A.index(2))

            # result[1:]
            if A[0] >= 4 and A[1] >= 4 and A[2] >= 4:
                return ""

            elif A[0] >= 4 and A[1] >= 4:
                result += str(A[2]) + ":"
                if A[0] >= 6 and A[1] >= 6:
                    return ""
                elif A[0] >= 6:
                    return result + str(A[1]) + str(A[0])
                else:
                    return result + str(A[0]) + str(A[1])

            elif A[0] >= 4:
                result += str(A[1]) + ":"
                if A[0] >= 6:
                    return result + str(A[2]) + str(A[0])
                else:
                    return result + str(A[0]) + str(A[2])

            else:
                return result + str(A[0]) + ":" + str(A[1]) + str(A[2])

        def startOne(A):
            result = ""
            result += '1'
            A.pop(A.index(1))

            result += str(A[0])
            A = A[1:]

            result += ":"

            if A[0] >= 6 and A[1] >= 6:
                return ""
            elif A[0] >= 6:
                return result + str(A[1]) + str(A[0])
            else:
                return result + str(A[0]) + str(A[1])
            return

        def startZero(A):
            result = ""
            result += '0'
            A.pop()

            result += str(A[0])
            A = A[1:]

            result += ":"

            if A[0] >= 6 and A[1] >= 6:
                return ""
            elif A[0] >= 6:
                return result + str(A[1]) + str(A[0])
            else:
                return result + str(A[0]) + str(A[1])
            return

        A.sort(reverse=True)

        if 2 in A:
            if A[0] >= 6 and A[1] >= 6 and 1 in A:
                total = startOne(A)
            elif A[0] >= 6 and A[1] >= 6 and 0 in A:
                total = startZero(A)
            else:
                total = startTwo(A)
        elif 1 in A:
            total = startOne(A)
        elif 0 in A:
            total = startZero(A)
        else:
            return ""
        return total
a = Solution()
print(a.largestTimeFromDigits([2,0,6,6]))

