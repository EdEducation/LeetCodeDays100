from typing import List

# Задача: 1855. Maximum Distance Between a Pair of Values
# Ссылка: https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/
# Сложность: Medium
# Тема: Два указателя / Бинарный поиск
#
# Описание:
# Даны два невозрастающих массива nums1 и nums2.
# Найти максимальное значение j - i, где 0 <= i < len(nums1), 0 <= j < len(nums2),
# i <= j и nums1[i] <= nums2[j].
# Если валидных пар нет, вернуть 0.
#
# Идея оптимального решения (O(n + m)):
# Используем два указателя: i по nums1, j по nums2.
# Для каждого i двигаем j вправо, пока nums2[j] >= nums1[i] (с учётом j >= i).
# Запоминаем максимальную разницу j - i.
#
# Альтернатива (O(n log m)): бинарный поиск для каждого i в nums2.


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        # Реализация будет добавлена здесь (PASS)
        pass


# Тесты
def run_tests():
    solution = Solution()
    
    # Тест 1: Пример из условия
    assert solution.maxDistance([55,30,5,4,2], [100,20,10,10,5]) == 2, "Тест 1 провален"
    
    # Тест 2: Пример из условия
    assert solution.maxDistance([2,2,2], [10,10,1]) == 1, "Тест 2 провален"
    
    # Тест 3: Пример из условия
    assert solution.maxDistance([30,29,19,5], [25,25,25,25,25]) == 2, "Тест 3 провален"
    
    # Тест 4: Нет валидных пар (все nums1[i] > nums2[j] при i <= j)
    assert solution.maxDistance([10,9,8], [5,4,3]) == 0, "Тест 4 провален"
    
    # Тест 5: Один элемент в каждом массиве
    assert solution.maxDistance([5], [10]) == 0, "Тест 5 провален"  # i=0, j=0, разница 0
    
    # Тест 6: Все элементы подходят, максимальная разница в конце
    assert solution.maxDistance([1,1,1], [5,5,5,5,5]) == 4, "Тест 6 провален"  # i=0, j=4
    
    # Тест 7: nums1 длиннее nums2
    assert solution.maxDistance([10,5,1], [4,3,2]) == 0, "Тест 7 провален"
    
    # Тест 8: nums2 длиннее nums1
    assert solution.maxDistance([3,2,1], [10,9,8,7,6]) == 4, "Тест 8 провален"  # i=0, j=4
    
    print("Все тесты пройдены!")


# Запуск тестов
if __name__ == "__main__":
    run_tests()