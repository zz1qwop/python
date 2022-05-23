# 46. Permutations
# https://leetcode.com/problems/permutations/

# 내 풀이
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(per, left_nums):
            if len(per) == len(nums):
                result.append(per)
                return
            for index, num in enumerate(left_nums):
                # per 배열을 그냥 사용하면 참조 때문에 오답이 되어 [:]를 사용했다.
                new_per = per[:]
                new_per.append(num)
                dfs(new_per, left_nums[0:index] + left_nums[index+1:])
        
        result = []
        for index, num in enumerate(nums):
            new_per = [num] 
            dfs(new_per, nums[0:index] + nums[index+1:])
            
        return result


# 1 DFS를 활용한 순열 생성
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        prev_elements = []

        def dfs(elements):
            if len(elements) == 0:
                results.append(prev_elements[:])

            # 순열 생성 재귀 호출
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop() # dfs가 끝나면 차례로 prev_element가 비워진다.

        dfs(nums)
        return results

# 2 itertools 모듈 사용
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(map(list, itertools.permutations(nums)))


'''
# 객체 복사
a = [1,2,3]
b = a
c = a[:]
d = a.copy()
id(a), id(b), id(c), id(d)
-> 43..52, 43..52, 43..48, 43..68

import copy
a = [1,2,[3,5],4]
b = copy.deepcopy(a)
id(a), id(b), b
-> 44..12, 44..24, [1,2,[3,5],4]
'''