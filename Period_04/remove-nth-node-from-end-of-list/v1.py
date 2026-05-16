# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
         # Создаем dummy-узел, чтобы упростить удаление головы
        dummy = ListNode(0, head)
        first = dummy
        second = dummy
        
        # Сдвигаем first на n шагов вперед
        for _ in range(n):
            first = first.next
        
        # Двигаем оба указателя, пока first не дойдет до конца
        while first.next:
            first = first.next
            second = second.next
        
        # Удаляем n-й узел с конца
        second.next = second.next.next
        
        # Возвращаем голову (dummy.next)
        return dummy.next