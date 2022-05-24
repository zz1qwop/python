# 77. Combinations
# https://leetcode.com/problems/combinations/

# 내 풀이
import itertools


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(combination, num):
            if len(combination) == k:
                result.append(combination)
                return
            if len(num) == 0:
                return
            
            for i, n in enumerate(num):
                new_com = combination[:]
                new_com.append(n)
                dfs(new_com, num[i+1:])
        
        result = []
        for i in range(1, n+1):
            combination = [i]
            dfs(combination, list(range(i+1, n+1)))
            
        return result


# 1 DFS로 k개 조합 생성
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
      results = []
      
      def dfs(elements, start: int, k: int):
        if k == 0:
          results.append(elements[:])
          return

        # 자신 이전의 모든 값을 고정하여 재귀 호출
        for i in range(start, n+1):
          elements.append(i)
          dfs(elements, i+1, k-1)
          elements.pop()

      dfs([], 1, k)
      return results

  
# 2 itertools 모듈 사용
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(itertools.combinations(range(1, n+1), k))