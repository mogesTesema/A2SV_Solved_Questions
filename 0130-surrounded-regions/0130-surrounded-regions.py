class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        """
        approach,
        first find bounded connections
        second mark X for each bounded

        """

        rows, cols = len(board),len(board[0])
        self.directions = [(1,0),(-1,0),(0,1),(0,-1)]
        self.marked = set()
        self.visited = set()

        def inbound(row,col):
            return 0 <= row < rows and 0 <= col < cols

        def mark_x():
            for row,col in self.visited:
                board[row][col] = "X"
                self.marked.add((row,col))
            

        def dfs(row,col):

            # if (row,col) in visited:
            #     return False

            self.visited.add((row,col))

            for move_row,move_col in self.directions:
                new_row,new_col = row + move_row, col + move_col
                if not inbound(new_row,new_col):
                    return False
                if (new_row,new_col) in self.visited:
                    continue
                if board[new_row][new_col] == "O":
                    if not dfs(new_row,new_col):
                        return False

            return True





        for row in range(rows):
            for col in range(cols):

                if board[row][col] == "O" and board[row][col] not in self.marked:
                    is_surrounded = dfs(row,col)

                    if is_surrounded:
                        mark_x()
                    self.visited.clear()

