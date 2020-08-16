class Solution:
    def orangesRotting(self, grid) -> int:
        self.errorRot = True
        def infest(list, row, col,errorRot):

            if row > 0 and list[row - 1][col] == 1:
                list[row - 1][col] = 2
                errorRot = False
            if row < len(list) - 1 and list[row + 1][col] == 1:
                list[row + 1][col] = 2
                errorRot = False
            if col > 0 and list[row][col - 1] == 1:
                list[row][col - 1] = 2
                errorRot = False
            if col < len(list[row]) - 1 and list[row][col + 1] == 1:
                list[row][col + 1] = 2
                errorRot = False
            return errorRot

        minute = 0
        while True:
            rottedRow = []
            rottedCol = []
            rottedAll = True

            # check rot apple
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if grid[i][j] == 2:
                        rottedRow.append(i)
                        rottedCol.append(j)
                    if grid[i][j] == 1:
                        rottedAll = False


            if rottedAll:
                return minute
            minute += 1

            # rotting
            errorRot = True
            for i in range(len(rottedCol)):
                errorRot = infest(grid, rottedRow[i], rottedCol[i],errorRot)
            if errorRot:
                return -1

        return minute

a = Solution()
print(a.orangesRotting([[1]]))
