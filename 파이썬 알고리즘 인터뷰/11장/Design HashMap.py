# 706. Design HashMap
# https://leetcode.com/problems/design-hashmap/

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

# 내 풀이
import collections


class MyHashMap:

    def __init__(self):
        self.key_map = []
        self.val_map = []

    def put(self, key: int, value: int) -> None:
        if key in self.key_map:
            index = self.key_map.index(key)
            self.val_map[index] = value
            return
        
        self.key_map.append(key)
        self.val_map.append(value)

    def get(self, key: int) -> int:
        if key in self.key_map:
            index = self.key_map.index(key)
            return self.val_map[index]
        
        return -1

    def remove(self, key: int) -> None:
        if key in self.key_map:
            index = self.key_map.index(key)
            self.key_map.pop(index)
            self.val_map.pop(index)


# 1 개별 체이닝 방식을 이용한 해시 테이블 구현

# 키, 값을 보관하고 연결 리스트로 처리할 별도의 객체
class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)
        # 각 ListNode를 담게 될 기본 자료형 선언.
        # 존재하지 않는 키를 조회할 경우 자동으로 디폴트를 생성해주는 collections.defaultdict 사용.

    def put(self, key:int, value:int ) -> None:
        index = key % self.size
        if self.table[index].value is None: # defaultdict을 사용했으므로 존재하지 않는 index일 경우 즉시 ListNode가 생성되기 때문에 .value를 비교
            self.table[index] = ListNode(key, value)
            return
        
        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p  = p.next
        p.next = ListNode(key, value)

    def get(self, key:int) -> int:
        index = key % self.size
        if self.table[index].value is None:
            return -1

        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    def remove(self, key:int) -> None:
        index = key % self.size
        if self.table[index].value is None:
            return

        # 1 인덱스의 첫 번째 노드일 때 삭제 처리
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return

        # 2 연결 리스트 노드 삭제
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next

# defaultdict()
# 인자로 주어진 객체의 기본값을 딕셔너리의 초깃값으로 지정할 수 있음.
# 참고 링크 : https://dongdongfather.tistory.com/69

from collections import defaultdict
int_dict = defaultdict(int)
print(int_dict) # defaultdict(<class 'int'>, {})

print(int_dict['key1']) # 0

int_dict['key2'] = 'test'
print(int_dict) # defaultdict(<class 'int'>, {'key1':0, 'key2':'test})