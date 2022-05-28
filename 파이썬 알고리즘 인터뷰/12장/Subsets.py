# 78. Subsets
# https://leetcode.com/problems/subsets/

from typing import List

# 내 풀이
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(index, num_array):
            result.append(num_array)
            for i in range(index+1, len(nums)):
                new_array = num_array[:]
                new_array.append(nums[i])
                dfs(i, new_array)
        
        result = []
        result.append([])
        
        for i, num in enumerate(nums):
            num_array = [num]
            new_array = num_array[:]
            dfs(i, new_array)
            
        return result

# 1 트리의 모든 DFS 결과
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(index, path):
            # 매번 결과 추가
            result.append(path)

            # 경로를 만들면서 DFS
            for i in range(index, len(nums)):
                dfs(i+1, path+[nums[i]])

        dfs(0, [])
        return result

'''
+ 연산자는 기존 리스트는 건드리지 않고 새로운 리스트를 반환한다.
'''