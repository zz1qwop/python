# 207. Course Schedule
# https://leetcode.com/problems/course-schedule/

from typing import List
import collections

# 1 DFS로 순환 구조 판별
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)

        traced = set()

        def dfs(i):
            # 순환 구조이면 False
            if i in traced:
                return False

            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False

            traced.remove(i)

            return True

        for x in list(graph):
            if not dfs(x):
                return False

        return True


# 2 가지치기를 이용한 최적화
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)

        traced = set()
        visited = set()

        def dfs(i):
            if i in traced:
                return False
            if i in visited:
                return True

            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
            
            traced.remove(i)
            visited.add(i)

            return True

        for x in list(graph):
            if not dfs(x):
                return False

        return True