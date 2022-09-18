class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        for crs, pre in prerequisites:
            graph[crs].append(pre)
        visit = set()
        def dfs(course):
            if course in visit:
                return False
            if graph[course] == []:
                return True
            visit.add(course)
            for pre in graph[course]:
                if not dfs(pre):
                    return False
            visit.remove(course)
            graph[course] = []
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True