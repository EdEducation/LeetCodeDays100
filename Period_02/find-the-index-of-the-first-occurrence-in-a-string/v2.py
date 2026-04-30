"""
Задача: Find the Index of the First Occurrence in a String (strStr)

Условие:
Даны две строки needle и haystack. Нужно вернуть индекс первого вхождения needle в haystack,
или -1, если needle не является подстрокой haystack.

Ограничения:
1 <= haystack.length, needle.length <= 10^4
Строки состоят только из строчных латинских букв.

Именованные алгоритмы:
1. Алгоритм Кнута-Морриса-Пратта (KMP) - O(n+m) времени, O(m) памяти
2. Алгоритм Бойера-Мура-Хорспула - обычно быстрее KMP на практике
3. Алгоритм Рабина-Карпа - O(n+m) в среднем с использованием хеширования
4. Встроенный метод str.find() в Python использует оптимизированный алгоритм
   (Boyer-Moore-Horspool с оптимизациями)

Точное решение за O(1) математически невозможно для данной задачи, 
так как требуется хотя бы просмотреть входные данные.
Лучшее возможное время - O(n*m) в худшем случае для наивного алгоритма,
и O(n+m) для KMP.

Рекомендуемый подход: использование встроенного метода find() - 
он использует оптимизированный C-код с алгоритмом Two-Way (используется в CPython).
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Возвращает индекс первого вхождения needle в haystack, или -1 если не найдено.
        
        Алгоритмическая сложность: O(n*m) в худшем случае (наивная реализация),
        но с использованием встроенного метода find() - O(n) в среднем.
        
        Args:
            haystack: строка, в которой производится поиск
            needle: искомая подстрока
            
        Returns:
            int: индекс первого вхождения или -1
        """
        if not needle:
            return 0
        
        n = len(haystack)
        m = len(needle)
        
        # Если needle длиннее haystack, сразу возвращаем -1
        if m > n:
            return -1
        
        # Пробегаем по всем возможным позициям начала
        for i in range(n - m + 1):
            # Проверяем совпадение подстроки
            if haystack[i:i + m] == needle:
                return i
        
        return -1


# Тесты
def run_tests():
    solution = Solution()
    
    # Тест 1: Начало строки
    assert solution.strStr("sadbutsad", "sad") == 0, "Тест 1 провален"
    
    # Тест 2: Подстрока не найдена
    assert solution.strStr("leetcode", "leeto") == -1, "Тест 2 провален"
    
    # Тест 3: Подстрока в середине
    assert solution.strStr("hello", "ll") == 2, "Тест 3 провален"
    
    # Тест 4: Подстрока равна всей строке
    assert solution.strStr("a", "a") == 0, "Тест 4 провален"
    
    # Тест 5: Пустая подстрока (по условию needle.length >= 1, но на всякий случай)
    # assert solution.strStr("abc", "") == 0, "Тест 5 провален"
    
    # Тест 6: needle длиннее haystack
    assert solution.strStr("abc", "abcd") == -1, "Тест 6 провален"
    
    # Тест 7: needle в конце haystack
    assert solution.strStr("hello world world", "world") == 6, "Тест 7 провален"
    
    # Тест 8: Одиночные символы
    assert solution.strStr("abcde", "e") == 4, "Тест 8 провален"
    
    # Тест 9: Повторяющиеся символы
    assert solution.strStr("aaaaa", "aaa") == 0, "Тест 9 провален"
    
    # Тест 10: Случай с перекрытием (needle перекрывается)
    assert solution.strStr("abababa", "aba") == 0, "Тест 10 провален"
    
    print("Все тесты пройдены!")


# Запуск тестов
if __name__ == "__main__":
    run_tests()