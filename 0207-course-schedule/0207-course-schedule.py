class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)

        for first, second in prerequisites:
            graph[second].append(first)

        visiting = set()   # current path
        visited = set()    # already safe

        def traverse(node):
            if node in visiting:
                return False   # cycle
            
            if node in visited:
                return True    # already checked
            
            visiting.add(node)

            for nbr in graph[node]:
                if not traverse(nbr):
                    return False

            visiting.remove(node)
            visited.add(node)

            return True

        for i in range(numCourses):
            if not traverse(i):
                return False

        return True