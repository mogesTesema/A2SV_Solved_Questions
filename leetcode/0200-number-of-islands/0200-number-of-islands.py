class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows, cols = len(grid),len(grid[0])
        self.directions = [(1,0),(-1,0),(0,1),(0,-1)]
        self.islands = 0


        def inbound(row,col):
            return 0 <= row < rows and 0 <= col < cols

        def dfs(row,col):
            if grid[row][col] == "0":
                return
            grid[row][col] = "0"

            for row_change,col_change in self.directions:
                new_row, new_col = row + row_change, col + col_change

                if inbound(new_row,new_col):
                    dfs(new_row,new_col)



        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    self.islands += 1
                    dfs(row,col)

        return self.islands
             






        