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
        
        Алгоритм Манакера (Manacher's Algorithm)
        Время: O(n), память: O(n)
        Оптимальное решение для очень длинных строк.
        """
        if not s or len(s) <= 1:
            return s
        
        # Преобразование строки: вставляем разделители
        # Например: "babad" -> "^#b#a#b#a#d#$"
        T = '#' + '#'.join(s) + '#'
        n = len(T)
        P = [0] * n  # Массив радиусов палиндромов
        
        center = right = 0
        
        for i in range(1, n - 1):
            # Зеркальная позиция относительно center
            mirror = 2 * center - i
            
            if i < right:
                P[i] = min(right - i, P[mirror])
            
            # Расширяем палиндром
            while i + P[i] + 1 < n and i - P[i] - 1 >= 0 and T[i + P[i] + 1] == T[i - P[i] - 1]:
                P[i] += 1
            
            # Обновляем center и right если нашли более правый палиндром
            if i + P[i] > right:
                center = i
                right = i + P[i]
        
        # Находим максимальный радиус и его центр
        max_radius = max(P)
        center_index = P.index(max_radius)
        
        # Восстанавливаем исходный палиндром
        start = (center_index - max_radius) // 2
        return s[start:start + max_radius]


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