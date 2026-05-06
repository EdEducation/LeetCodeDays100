class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Находит самую длинную палиндромную подстроку в строке s.
        
        Известные алгоритмы:
        1. "Expand Around Center" - расширение от центра (O(n²), O(1) памяти)
        2. Алгоритм Манакера (Manacher's Algorithm) - O(n) времени, O(n) памяти
           Это оптимальное решение для данной задачи. Алгоритм использует 
           симметрию палиндромов и обрабатывает как четные, так и нечетные 
           палиндромы за линейное время.
        
        Для n ≤ 1000 подойдет любой алгоритм O(n²), но Манакер даёт лучшее 
        асимптотическое время O(n).
        """
        pass


# Тесты
def run_tests():
    solution = Solution()
    
    # Тест 1: babad → "bab" или "aba"
    result1 = solution.longestPalindrome("babad")
    assert result1 in ["bab", "aba"], f"Тест 1 провален: {result1}"
    
    # Тест 2: cbbd → "bb"
    assert solution.longestPalindrome("cbbd") == "bb", "Тест 2 провален"
    
    # Тест 3: Одиночный символ
    assert solution.longestPalindrome("a") == "a", "Тест 3 провален"
    
    # Тест 4: Все символы одинаковые
    assert solution.longestPalindrome("aaaa") == "aaaa", "Тест 4 провален"
    
    # Тест 5: Палиндром нечетной длины
    assert solution.longestPalindrome("racecar") == "racecar", "Тест 5 провален"
    
    # Тест 6: Пустая строка (не по условию, но для проверки)
    # assert solution.longestPalindrome("") == "", "Тест 6 провален"
    
    # Тест 7: Строка из двух разных символов
    assert solution.longestPalindrome("ab") in ["a", "b"], "Тест 7 провален"
    
    print("Все тесты пройдены!")


# Запуск тестов
if __name__ == "__main__":
    run_tests()