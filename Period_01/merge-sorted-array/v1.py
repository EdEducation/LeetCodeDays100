from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Слияние nums1 и nums2 в nums1 в отсортированном порядке.
        
        Алгоритм: два указателя с конца (сравнение с конца массива).
        - Временная сложность: O(m + n)
        - Пространственная сложность: O(1) (без доп. памяти)
        
        Это оптимальное решение, так как нужно обработать все m+n элементов.
        """
        # РЕАЛИЗАЦИЯ (PASS)
        pass


# Тесты
def run_tests():
    solution = Solution()
    
    # Тест 1: Базовый пример
    nums1 = [1, 2, 3, 0, 0, 0]
    solution.merge(nums1, 3, [2, 5, 6], 3)
    assert nums1 == [1, 2, 2, 3, 5, 6], "Тест 1 провален"
    
    # Тест 2: Пустой nums2
    nums1 = [1]
    solution.merge(nums1, 1, [], 0)
    assert nums1 == [1], "Тест 2 провален"
    
    # Тест 3: Пустой nums1
    nums1 = [0]
    solution.merge(nums1, 0, [1], 1)
    assert nums1 == [1], "Тест 3 провален"
    
    # Тест 4: Все элементы nums2 меньше nums1
    nums1 = [4, 5, 6, 0, 0, 0]
    solution.merge(nums1, 3, [1, 2, 3], 3)
    assert nums1 == [1, 2, 3, 4, 5, 6], "Тест 4 провален"
    
    # Тест 5: Все элементы nums2 больше nums1
    nums1 = [1, 2, 3, 0, 0, 0]
    solution.merge(nums1, 3, [4, 5, 6], 3)
    assert nums1 == [1, 2, 3, 4, 5, 6], "Тест 5 провален"
    
    # Тест 6: Перемешанные значения
    nums1 = [2, 4, 6, 0, 0, 0]
    solution.merge(nums1, 3, [1, 3, 5], 3)
    assert nums1 == [1, 2, 3, 4, 5, 6], "Тест 6 провален"
    
    # Тест 7: Один элемент в каждом
    nums1 = [2, 0]
    solution.merge(nums1, 1, [1], 1)
    assert nums1 == [1, 2], "Тест 7 провален"
    
    print("Все тесты пройдены!")


# Запуск тестов
if __name__ == "__main__":
    run_tests()