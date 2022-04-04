# 21. Merge Two Sorted Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 내 풀이
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        results = ListNode()
        results_node = results
        
        while list1 !=None and list2 != None:
            if list1.val <= list2.val:
                results.next = list1
                results = results.next
                list1 = list1.next
            else:
                results.next = list2
                results = results.next
                list2 = list2.next
                
        if list1 == None:
            while list2 != None:
                results.next = list2
                results = results.next
                list2 = list2.next
        else:
            while list1 != None:
                results.next = list1
                results = results.next
                list1 = list1.next
                
        results_node = results_node.next
        return results_node


# 1 재귀 구조로 연결
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (not list1) or (list2 and list1.val > list2.val): # list1이 None or list2가 None이 아니고 list1 값이 더 클 때
            list1, list2 = list2, list1
        if list1:
            list1.next = self.mergeTwoLists(list1.next, list2)
        return list1
        # 값이 작은 것을 list1.next에 연결해준다.
        # list1이 값이 작을 때 : list1.next와 list2 중에 더 작은 것을 자신의 뒤로 연결
        # list1이 None이면 -> list1에 있는 값들이 다 list2의 값보다 작아서 이제 비교할 필요가 x. 그냥 가져다 붙이는 듯
        # 재귀니까 return 되면서 원래 순서대로?
