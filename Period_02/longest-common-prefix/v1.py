# https://leetcode.com/problems/longest-common-prefix/submissions/1993206797/

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""

        # Находим минимальную длину
        min_length = len(min(strs, key=len))
        
        for i in range (min_length):
            chars = [s[i] for s in strs] # не используем контроль длины, так как получили это ранее
            if len(set(chars)) > 1:
                break

            result += chars[0]

        return result

# Тесты
def run_tests():
    solution = Solution()
    
    # Тест 1: Базовый пример
    assert solution.longestCommonPrefix(["flower","flow","flight"]) == "fl", "Тест 1 провален"
    
    # Тест 2: Нет общего префикса
    assert solution.longestCommonPrefix(["dog","racecar","car"]) == "", "Тест 2 провален"
    
    # Тест 3: Одна строка
    assert solution.longestCommonPrefix(["single"]) == "single", "Тест 3 провален"
    
    # Тест 4: Пустая строка в массиве
    assert solution.longestCommonPrefix(["", "test"]) == "", "Тест 4 провален"
    
    # Тест 5: Все строки одинаковые
    assert solution.longestCommonPrefix(["same","same","same"]) == "same", "Тест 5 провален"
    
    # Тест 6: Пустой массив (хотя по условию strs.length >= 1)
    # assert solution.longestCommonPrefix([]) == "", "Тест 6 провален"
    
    print("Все тесты пройдены!")


# Запуск тестов
if __name__ == "__main__":
    run_tests()