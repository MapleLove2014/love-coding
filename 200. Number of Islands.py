class Solution:
    def numIslands(self, grid) -> int:
        def isWater(grid, i, j):
            return i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] == "0"

        def go(grid, i, j, visited, directions):
            if isWater(grid, i, j) or visited[i][j]:
                return
            visited[i][j] = True
            for d in directions:
                go(grid, i + d[0], j + d[1], visited, directions)
        
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        c = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if not isWater(grid, i, j) and not visited[i][j]:
                    c += 1
                    go(grid, i, j, visited, directions)
        return c
    
s = Solution()
print(s.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))

