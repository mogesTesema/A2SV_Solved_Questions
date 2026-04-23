class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        # -1: uncolored, 1: black, 0: green
        blacks = set()
        greens = set()

        def dfs(node, color):
            #  check if already colored → must match expected color
            if node in blacks:
                return color == 1
            if node in greens:
                return color == 0

            # assign color
            if color == 1:
                blacks.add(node)
            else:
                greens.add(node)

            # visit ALL neighbors (no early return inside loop)
            for nbr in graph[node]:
                if not dfs(nbr, 1 - color):
                    return False

            return True

        #  handle disconnected graph
        for i in range(len(graph)):
            if i not in blacks and i not in greens:
                if not dfs(i, 0):
                    return False

        return True