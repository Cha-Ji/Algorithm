class Solution:
    def partitionLabels(self, S: str):
        set_input = set(S)
        part = [[0]] * len(set_input)
        s_length = len(S)
        i = 0
        while set_input:
            element = set_input.pop()

            # 알파벳의 시작과 끝지점을 구한다.
            start = S.index(element)
            end = s_length - S[::-1].index(element) - 1
            part[i] = [start, end]
            i += 1

        # 겹치는 구간을 통일한다.
        part = sorted(part[:i], reverse=True)
        i -= 1
        while i > 0:
            j = i - 1
            while j >= 0:
                if part[i][0] < part[j][0] < part[i][1]:
                    part[j][0] = part[i][0]
                    part[j][1] = max(part[i][1], part[j][1])
                    part[i] = [-1, -1]
                j -= 1
            i -= 1

        # 각 구간의 길이를 구한다.
        result = []

        for i in range(len(part)-1, -1, -1):
            if part[i][1] > -1:
                result.append(part[i][1] - part[i][0] + 1)

        return result
a = Solution()
print(a.partitionLabels("ababcbacadefegdehijhklij"))
print(a.partitionLabels("caedbdedda"))
print(a.partitionLabels("bbvemgjwruuwalp"))
