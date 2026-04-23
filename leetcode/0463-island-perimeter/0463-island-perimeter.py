class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])

        self.directions = [(1,0),(-1,0),(0,1),(0,-1)]
        self.perimeters = 0

        def inbound(row,col):
            return 0 <= row < rows and 0 <= col < cols
        
        visited = set()
        def dfs(row, col):
            if (row,col) in visited:
                return 
                
            visited.add((row,col))
            for x,y  in self.directions:
                new_row, new_col = x + row, y + col

                if not inbound(new_row,new_col) or grid[new_row][new_col] == 0:
                    self.perimeters += 1
                elif inbound(new_row,new_col) and grid[new_row][new_col] == 1:

                    if (new_row,new_col) not in visited:
                        dfs(new_row,new_col)

        
        for row in range(rows):
            for col in range(cols):

                if grid[row][col] == 1:
                    dfs(row,col)
                    break

        return self.perimeters
