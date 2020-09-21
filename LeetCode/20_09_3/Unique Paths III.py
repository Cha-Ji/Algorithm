class Solution:
    def uniquePathsIII(self, grid) -> int:
        self.xlen = len(grid)
        self.ylen = len(grid[0])
        self.result = 0
        def dfs(x, y):
            # indexing error
            if x >= self.xlen or x < 0\
                    or y >= self.ylen or y < 0:
                return

            # cannot walk
            if grid[x][y] == -1:
                return
            # end
            if grid[x][y] == 2:
                for i in grid:
                    if i.count(0) > 0:
                        return
                self.result += 1
                return
            # dfs
            temp = grid[x][y]
            grid[x][y] = -1
            dfs(x + 1, y)
            dfs(x, y + 1)
            dfs(x - 1, y)
            dfs(x, y - 1)
            grid[x][y] = temp
            
        # main()
        for i in range(self.xlen):
            for j in range(self.ylen):
                if grid[i][j] == 1:
                    dfs(i, j)
                    break
        return self.result
a = Solution()
print(a.uniquePathsIII([[0,1],[2,0]]))
