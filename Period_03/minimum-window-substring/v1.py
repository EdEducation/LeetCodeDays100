"""
Задача: Minimum Window Substring (LeetCode 76)

Алгоритмический подход: Скользящее окно (Sliding Window) с двумя указателями
и счетчиками символов. Это классическое решение с временной сложностью O(m + n).

Известный алгоритм: нет математической формулы O(1), но есть оптимальное
решение за линейное время с использованием хэш-таблиц и техники "расширения
и сжатия" окна.

Временная сложность: O(|s| + |t|)
Пространственная сложность: O(|t|) для хранения счетчиков
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        # Словарь для подсчета необходимых символов из t
        need = {}
        for char in t:
            need[char] = need.get(char, 0) + 1
        
        # Словарь для подсчета символов в текущем окне
        window = {}
        
        # Указатели окна
        left = 0
        right = 0
        
        # Переменные для отслеживания минимального окна
        min_len = float('inf')
        min_left = 0
        
        # Количество уникальных символов, которые мы уже удовлетворили
        have = 0
        need_unique = len(need)
        
        while right < len(s):
            # Расширяем окно вправо
            char = s[right]
            window[char] = window.get(char, 0) + 1
            
            # Если текущий символ нужен и его количество достигло требуемого
            if char in need and window[char] == need[char]:
                have += 1
            
            # Пытаемся сжать окно слева, пока у нас есть все нужные символы
            while have == need_unique:
                # Обновляем минимальное окно
                current_len = right - left + 1
                if current_len < min_len:
                    min_len = current_len
                    min_left = left
                
                # Удаляем левый символ из окна
                left_char = s[left]
                window[left_char] -= 1
                
                # Если после удаления нам не хватает этого символа
                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1
                
                # Сдвигаем левый указатель
                left += 1
            
            # Расширяем правый указатель
            right += 1
        
        # Возвращаем результат
        if min_len == float('inf'):
            return ""
        return s[min_left:min_left + min_len]    


# Тесты
def run_tests():
    solution = Solution()
    
    # Тест 1: Базовый пример
    assert solution.minWindow("ADOBECODEBANC", "ABC") == "BANC", "Тест 1 провален"
    
    # Тест 2: Один символ
    assert solution.minWindow("a", "a") == "a", "Тест 2 провален"
    
    # Тест 3: Невозможный случай (два 'a' в t, но в s только один)
    assert solution.minWindow("a", "aa") == "", "Тест 3 провален"
    
    # Тест 4: t длиннее s
    assert solution.minWindow("abc", "abcd") == "", "Тест 4 провален"
    
    # Тест 5: Все символы совпадают
    assert solution.minWindow("aa", "aa") == "aa", "Тест 5 провален"
    
    # Тест 6: Строка уже является минимальным окном
    assert solution.minWindow("abc", "abc") == "abc", "Тест 6 провален"
    
    # Тест 7: Символы не в порядке - неверный тест
    #assert solution.minWindow("aefbc", "abc") == "abc", "Тест 7 провален"
    
    # Тест 8: Пустое окно
    assert solution.minWindow("", "a") == "", "Тест 8 провален"
    
    # Тест 9: Повторяющиеся символы в t
    assert solution.minWindow("abbbbbbc", "abc") == "abbbbbbc", "Тест 9 провален"
    
    # Тест 10: Большой алфавит (верхний и нижний регистр)
    assert solution.minWindow("aAbBcC", "ABC") == "AbBcC", "Тест 10 провален"
    
    print("Все тесты пройдены!")


# Запуск тестов
if __name__ == "__main__":
    run_tests()