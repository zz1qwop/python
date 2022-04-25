# 23. Merge k Sorted Lists
# https://leetcode.com/problems/merge-k-sorted-lists/


# 1 우선순위 큐를 이용한 리스트 병합
def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    root = result = ListNode(None)
    heap = []

    # 각 연결 리스트의 루트를 힙에 저장
    for i in range(len(lists)):
        if lists[i]: # 해당 if문을 안 써주면 테스트 케이스가 [[]] 일 때 틀리게 된다.
            heapq.heappush(heap, (lists[i].val, i, lists[i]))

        # 힙 추출 이후 다음 노드는 다시 저장
        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            result.next = node[2]

            result = result.next
            if result.next:
                heaqp.heappush(heap, (result.next.val, idx, result.next))

        return root.next

'''
어차피 맨 앞 노드끼리만 비교하게 되므로 heapq에는 제일 맨 앞 ListNode만 넣어줌
해당 ListNode가 빠지면, .next가 존재할 경우 .next를 heapq에 집어넣는다.
'''

'''
PriorityQueue vs heapq
파이썬의 PriorityQueue는 내부적으로 heapq를 사용하도록 구현되어 있다.
둘의 차이점은 PriorityQueue가 스레드 세이프 클래스라는 점이며,
heapq 모듈은 스레드 세이프를 보장하지 않는다는 점이다.
파이썬은 GIL의 특성상 멀티 스레딩이 거의 의미가 없기 때문에 대부분 멀티 프로세싱으로 활용한다.

파이썬 전역 인터프리터 락(GIL)
: 하나의 스레드가 자원을 독점하는 형태로 실행. 
'''
