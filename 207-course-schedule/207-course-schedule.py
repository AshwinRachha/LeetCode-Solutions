class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = defaultdict(list)
        for course, prereq in prerequisites:
            prereqs[course].append(prereq)
        seen = set()
        def dfs(course):
            if course in seen:
                return False
            if prereqs[course] == []:
                return True
            seen.add(course)
            for c in prereqs[course]:
                if not dfs(c):
                    return False
            seen.remove(course)
            prereqs[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course): return False
        return True