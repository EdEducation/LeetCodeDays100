from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # реализовать
        pass


def create_linked_list(arr):
    """Вспомогательная функция для создания связного списка из массива"""
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(head):
    """Вспомогательная функция для преобразования связного списка в массив"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


# Тесты
def run_tests():
    solution = Solution()
    
    # Тест 1: Базовый пример
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    result = solution.mergeTwoLists(list1, list2)
    assert linked_list_to_list(result) == [1, 1, 2, 3, 4, 4], "Тест 1 провален"
    
    # Тест 2: Оба списка пустые
    list1 = create_linked_list([])
    list2 = create_linked_list([])
    result = solution.mergeTwoLists(list1, list2)
    assert linked_list_to_list(result) == [], "Тест 2 провален"
    
    # Тест 3: Первый список пустой, второй с одним элементом
    list1 = create_linked_list([])
    list2 = create_linked_list([0])
    result = solution.mergeTwoLists(list1, list2)
    assert linked_list_to_list(result) == [0], "Тест 3 провален"
    
    # Тест 4: Первый список с одним элементом, второй пустой
    list1 = create_linked_list([5])
    list2 = create_linked_list([])
    result = solution.mergeTwoLists(list1, list2)
    assert linked_list_to_list(result) == [5], "Тест 4 провален"
    
    # Тест 5: Списки разной длины
    list1 = create_linked_list([1, 3, 5, 7])
    list2 = create_linked_list([2, 4, 6])
    result = solution.mergeTwoLists(list1, list2)
    assert linked_list_to_list(result) == [1, 2, 3, 4, 5, 6, 7], "Тест 5 провален"
    
    # Тест 6: Отрицательные числа
    list1 = create_linked_list([-5, -2, 0, 3])
    list2 = create_linked_list([-4, -1, 2, 5])
    result = solution.mergeTwoLists(list1, list2)
    assert linked_list_to_list(result) == [-5, -4, -2, -1, 0, 2, 3, 5], "Тест 6 провален"
    
    # Тест 7: Один список длиннее другого
    list1 = create_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    list2 = create_linked_list([0])
    result = solution.mergeTwoLists(list1, list2)
    assert linked_list_to_list(result) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "Тест 7 провален"
    
    # Тест 8: Все элементы равны
    list1 = create_linked_list([2, 2, 2])
    list2 = create_linked_list([2, 2, 2, 2])
    result = solution.mergeTwoLists(list1, list2)
    assert linked_list_to_list(result) == [2, 2, 2, 2, 2, 2, 2], "Тест 8 провален"
    
    print("Все тесты пройдены!")


# Запуск тестов
if __name__ == "__main__":
    run_tests()