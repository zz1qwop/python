# 39. Combination Sum
# https://leetcode.com/problems/combination-sum/

# 내 풀이
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(result, can_array, index):
            if sum(can_array) > target:
                return
            elif sum(can_array) == target:
                result.append(can_array[:])
            
            for i in range(index, len(candidates)):
                can_array.append(candidates[i])
                dfs(result, can_array, index)
                can_array.pop()
                index += 1
        
        result = []
        can_array = []
        dfs(result, can_array, 0)
        
        return result


# 1 DFS로 중복 조합 그래프 탐색
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(csum, index, path):
            # 종료 조건
            if csum < 0:
                return
            if csum == 0:
                result.append(path)
                return

            # 자신부터 하위 원소까지의 나열 재귀 호출
            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], i, path+[candidates[i]])

        dfs(target, 0, [])
        return result