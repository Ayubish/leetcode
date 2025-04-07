class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def dfs(node, visited):
            if node == destination:
                return True

            visited.add(node)

            for neigbour in graph[node]:
                if neigbour not in visited:
                    found = dfs(neigbour, visited)

                    if found:
                        return True

            return False
        
        graph = defaultdict(list)

        for pair in edges:
            graph[pair[0]].append(pair[1])
            graph[pair[1]].append(pair[0])

        visited = set()

        return dfs(source, visited)
    