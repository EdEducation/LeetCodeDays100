# Given a string s, find the length of the longest substring without duplicate characters.
# 
# Примеры:
# Input: s = "abcabcbb" -> Output: 3 ("abc")
# Input: s = "bbbbb" -> Output: 1 ("b")
# Input: s = "pwwkew" -> Output: 3 ("wke")
#
# Оптимальное решение: скользящее окно + хэш-таблица (сложность O(n), память O(min(n, алфавит)))


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # реализовать
        pass


# Тесты
def run_tests():
    solution = Solution()
    
    # Тест 1: Обычный случай с повторениями
    assert solution.lengthOfLongestSubstring("abcabcbb") == 3, "Тест 1 провален"
    
    # Тест 2: Все одинаковые символы
    assert solution.lengthOfLongestSubstring("bbbbb") == 1, "Тест 2 провален"
    
    # Тест 3: С пробелами и символами
    assert solution.lengthOfLongestSubstring("pwwkew") == 3, "Тест 3 провален"
    
    # Тест 4: Пустая строка
    assert solution.lengthOfLongestSubstring("") == 0, "Тест 4 провален"
    
    # Тест 5: Все символы уникальны
    assert solution.lengthOfLongestSubstring("abcde") == 5, "Тест 5 провален"
    
    # Тест 6: Специальные символы и цифры
    assert solution.lengthOfLongestSubstring("ab!@#ab!@#") == 5, "Тест 6 провален"
    
    # Тест 7: Длинная строка с дубликатами
    assert solution.lengthOfLongestSubstring("dvdf") == 3, "Тест 7 провален"
    
    print("Все тесты пройдены!")


# Запуск тестов
if __name__ == "__main__":
    run_tests()