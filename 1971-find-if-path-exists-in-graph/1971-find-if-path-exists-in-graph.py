class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph_list = defaultdict(list)
        visited = set()

        for v,u in edges:
            graph_list[v].append(u)
            graph_list[u].append(v)
        print(graph_list)
        def explore(node):
            nonlocal visited
            visited.add(node)
            if node == destination:
                return True
            
            for nbr in graph_list[node]:
                if nbr not in visited:

                    found = explore(nbr)

                    if found:
                        return True
            return False
        return explore(source)
