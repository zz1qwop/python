# 347. Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/

# 내 풀이
import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = collections.Counter(nums)
        common_array = my_dict.most_common(k)
        result = []
        
        for key, _ in common_array:
            result.append(key)
            
        return result

# collections.Counter.most_common(n)
# 많은 순으로 정렬한 배열 리턴. [(key, val)]. 개수는 n으로 지정 가능하다.
# https://docs.python.org/3/library/collections.html#collections.Counter

# 1 Counter를 이용한 음수 순 추출
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = collections.Counter(nums)
        freqs_heap = []
        # 힙에 음수로 삽입
        for f in freqs:
            heapq.heappush(freqs_heap, (-freqs[f], f))

        topk = list()
        # k번 만큼 추출, 최소 힙이므로 가장 작은 음수 순으로 추출
        for _ in range(k):
            topk.append(heapq.heqppop(freqs_heap)[1])

        return topk

# 2 파이썬다운 방식
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return list(zip(*collections.Counter(nums).most_common(k)))[0]

'''
## zip() 함수
- zip() 함수는 2개 이상의 시퀀스를 짧은 길이를 기준으로 일대일 대응하는
  새로운 튜플 시퀀스를 만드는 역할을 한다.
  a = [1,2,3,4,5]
  b = [2,3,4,5]
  c = [3,4,5]

  list(zip(a,b)) : [(1,2), (2,3), (3,4), (4,5)]
  list(zip(a,b,c)) : [(1,2,3), (2,3,4), (3,4,5)]

  이처럼 zip()은 여러 시퀀스에서 동일한 인덱스의 아이템을 순서대로 추출하여
  튜플로 만들어 준다.

## 아스테리스크(*)
- 파이썬에서 *는 언팩이다.
- 시퀀스 언패킹 연산자 : 시퀀스를 풀어헤치는 연산자. 주로 튜플이나 리스트를 언패킹.
  collections.Counter(nums).most_common(k)
  [(1,3), (2,2)]

  - 언패킹 했을 때
  list(zip(*collections.Counter(nums).most_common(k)))
  : [(1,2), (3,2)]
  - 언패킹 안 했을 때
  list(zip(collections.Counter(nums).most_common(k)))
  [((1,3),), ((2,2),)]
  -> 튜플이 풀어지지 않고 하나의 값처럼 묶였음.

- 예제
  fruits = ['lemon', 'pear', 'watermelon', 'tomato']
  print(fruits[0], fruits[1], fruits[2], fruits[3])
  : lemon pear watermelon tomato
  print(*fruits)
  : lemon pear watermelon tomato

- 함수의 파라미터가 되었을 때는 반대로 패킹도 가능하다.
  def f(*params):
      print(params)

- 변수의 할당
  a, *b = [1,2,3,4]
  a : 1
  b : [2,3,4]
  *a, b = [1,2,3,4]
  a : [1,2,3]
  b : 4

- ** : 키, 값 페어 언패킹
  date_info = {'year':'2022', 'month':'05', 'day':'01'}
  new_info = {**date_info, 'day':'14'}
  new_info : {'year':'2022', 'month':'05', 'day':'14'}
  **date_info에 모든 요소를 언패킹할 수 있으며 새로운 값도 업데이트 했다.
'''