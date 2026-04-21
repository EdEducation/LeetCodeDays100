from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Удаляет дубликаты из отсортированного массива in-place.
        Использует while, а не for range для избежания аллокации лишней памяти.
        """
        if not nums:
            return 0
        
        i = 0  # указатель на последний уникальный элемент
        j = 1  # указатель для перебора
        length = len(nums) # вычисляем 1 раз
        
        while j < length:
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
            j += 1
        
        return i + 1


def run_tests():
    solution = Solution()
    
    # Тест 1: Пример из условия
    nums1 = [1, 1, 2]
    k1 = solution.removeDuplicates(nums1)
    assert k1 == 2, f"Тест 1 провален: ожидалось 2, получено {k1}"
    assert nums1[:k1] == [1, 2], f"Тест 1 провален: массив {nums1[:k1]}"
    
    # Тест 2: Пример из условия
    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k2 = solution.removeDuplicates(nums2)
    assert k2 == 5, f"Тест 2 провален: ожидалось 5, получено {k2}"
    assert nums2[:k2] == [0, 1, 2, 3, 4], f"Тест 2 провален: массив {nums2[:k2]}"
    
    # Тест 3: Все элементы одинаковые
    nums3 = [1, 1, 1, 1]
    k3 = solution.removeDuplicates(nums3)
    assert k3 == 1, f"Тест 3 провален: ожидалось 1, получено {k3}"
    assert nums3[:k3] == [1], f"Тест 3 провален: массив {nums3[:k3]}"
    
    # Тест 4: Все элементы уникальны
    nums4 = [1, 2, 3, 4, 5]
    k4 = solution.removeDuplicates(nums4)
    assert k4 == 5, f"Тест 4 провален: ожидалось 5, получено {k4}"
    assert nums4[:k4] == [1, 2, 3, 4, 5], f"Тест 4 провален: массив {nums4[:k4]}"
    
    # Тест 5: Один элемент
    nums5 = [42]
    k5 = solution.removeDuplicates(nums5)
    assert k5 == 1, f"Тест 5 провален: ожидалось 1, получено {k5}"
    assert nums5[:k5] == [42], f"Тест 5 провален: массив {nums5[:k5]}"
    
    # Тест 6: Отрицательные числа
    nums6 = [-3, -3, -2, -1, -1, 0]
    k6 = solution.removeDuplicates(nums6)
    assert k6 == 4, f"Тест 6 провален: ожидалось 4, получено {k6}"
    assert nums6[:k6] == [-3, -2, -1, 0], f"Тест 6 провален: массив {nums6[:k6]}"
    
    print("Все тесты пройдены!")


if __name__ == "__main__":
    run_tests()