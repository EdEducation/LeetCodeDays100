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
        """
        Находит длину самой длинной подстроки без повторяющихся символов.
        
        Алгоритм: скользящее окно (sliding window) с двумя указателями.
        
        Args:
            s: входная строка
            
        Returns:
            int: максимальная длина подстроки без повторений
        """
        
        # Словарь для хранения последней позиции каждого символа
        # Ключ: символ, Значение: индекс его последнего вхождения
        char_index_map = {}
        
        # Левый указатель окна (начало текущей рассматриваемой подстроки)
        left = 0
        
        # Максимальная найденная длина
        max_length = 0
        
        # Правый указатель движется по строке
        for right in range(len(s)):
            current_char = s[right]
            
            # Если символ уже встречался и его последняя позиция внутри текущего окна
            # (то есть >= left), то нужно сдвинуть левый указатель
            if current_char in char_index_map and char_index_map[current_char] >= left:
                # Перемещаем левый указатель на позицию после предыдущего вхождения дубликата
                left = char_index_map[current_char] + 1
            
            # Обновляем последнюю позицию текущего символа
            char_index_map[current_char] = right
            
            # Вычисляем длину текущего окна и обновляем максимум
            current_length = right - left + 1
            max_length = max(max_length, current_length)
        
        return max_length


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