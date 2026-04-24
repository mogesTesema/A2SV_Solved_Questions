class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        seen = set()

        def inbound(r, c):
            return 0 <= r < rows and 0 <= c < cols

        def dfs(r, c, visited):
            if (r, c) in visited:
                return True

            visited.add((r, c))
            seen.add((r, c))

            is_surrounded = True

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not inbound(nr, nc):
                    is_surrounded = False
                    continue

                if board[nr][nc] == "O":
                    if not dfs(nr, nc, visited):
                        is_surrounded = False

            return is_surrounded

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r,c) not in seen:
                    visited = set()
                    if dfs(r, c, visited):
                        for vr, vc in visited:
                            board[vr][vc] = "X"