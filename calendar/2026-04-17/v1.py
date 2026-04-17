

from typing import List

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        last_index = {}
        min_distance = float('inf')
        
        for i, num in enumerate(nums):
            # Если текущее число уже встречалось как реверс какого-то предыдущего
            if num in last_index:
                distance = i - last_index[num]
                min_distance = min(min_distance, distance)
            
            # Сохраняем реверс текущего числа с его индексом
            reversed_num = int(str(num)[::-1])
            last_index[reversed_num] = i
        
        return min_distance if min_distance != float('inf') else -1


# Тесты
def run_tests():
    solution = Solution()
    
    # Тест 1
    assert solution.minMirrorPairDistance([12, 21, 45, 33, 54]) == 1, "Тест 1 провален"
    
    # Тест 2
    assert solution.minMirrorPairDistance([120, 21]) == 1, "Тест 2 провален"
    
    # Тест 3
    assert solution.minMirrorPairDistance([21, 120]) == -1, "Тест 3 провален"
    
    # Дополнительные тесты
    assert solution.minMirrorPairDistance([1, 2, 3, 4, 5]) == -1, "Тест 4 провален"
    
    assert solution.minMirrorPairDistance([12, 21, 12, 21]) == 1, "Тест 5 провален"
    
    assert solution.minMirrorPairDistance([123, 321, 123, 321]) == 1, "Тест 6 провален"
    
    assert solution.minMirrorPairDistance([10, 1, 10]) == 1, "Тест 7 провален"
    
    assert solution.minMirrorPairDistance([120, 21, 120, 21]) == 1, "Тест 8 провален"
    
    print("Все тесты пройдены!")


# Запуск тестов
if __name__ == "__main__":
    run_tests()