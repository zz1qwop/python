# 1. Two Sum

from typing import List

# 1 브루트 포스로 계산 : 일일이 확인해보는 무차별 대입 방식
'''
class Solution:
    def twoSum(self, nums:List[int], target:int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

- 시간 복잡도 : O(n^2)
'''

# 2 in을 이용한 탐색
'''
class Solution:
    def twoSum(self, nums:List[int], target:int) -> List[int]:
        for i, n in enumerate(nums):# enumerate : index와 원소
            complement = target -  n

            if complement in nums[i+1:]:
                return [nums.index(n), nums[i+1:].index(complement) + (i+1)]

- in의 시간 복잡도 : O(n), 전체 시간 복잡도 : O(n^2)
'''

# 3 첫 번째 수를 뺀 결과 키 조회
'''
class Solution:
    def twoSum(self, nums:List[int], target:int) -> List[int]:
        nums_map = {}
        # 키와 값을 바꿔서 딕셔너리로 저장
        for i, num in enumerate(nums):
            nums_map[num] = i

        # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
        for i, num in enumerate(nums):
            if target-num in nums_map and i != nums_map[target-num]:
                return [i, nums_map[target-num]]

- 시간 복잡도 : O(n)
'''

# 4 조회 구조 개선

class Solution:
    def twoSum(self, nums:List[int], target:int) -> List[int]:
        nums_map = {}
        # 하나의 for문으로 통합
        for i, num in enumerate(nums):
            if target-num in nums_map:
                return [nums_map[target-num], i]
            nums_map[num] = i
        # 3번과 성능 상의 큰 차이는 없지만 코드가 간결해짐


# 5 투 포인터 이용
'''
class Solution:
    def twoSum(self, nums:List[int], target:int) -> List[int]:
        nums.sort()
        left, right = 0, len(nums)-1
        while not left == right:
            # 합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로
            if nums[left] + nums[right] < target:
                left += 1
            # 합이 타겟보다 크면 오른쪽 포인터를 왼쪽으로
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                return [left, right]

- 불가능한 풀이 : sort를 실행하면 인덱스가 섞인다.
'''

nums = list(map(int, input("nums : ").split()))
target = int(input("target : "))
c = Solution()
result = c.twoSum(nums, target)
print(result)
