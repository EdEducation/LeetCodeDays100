"""
Задача: Длина последнего слова
Дана строка s, состоящая из слов и пробелов.
Нужно вернуть длину последнего слова в строке.

Слово - максимальная подстрока, состоящая только из непробельных символов.

Constraints:
- 1 <= s.length <= 10^4
- s состоит только из английских букв и пробелов ' '
- В строке есть хотя бы одно слово
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        Возвращает длину последнего слова в строке.
        
        Алгоритм:
        - Идем с конца строки, пропускаем пробелы
        - Считаем символы последнего слова
        
        Временная сложность: O(n)
        Пространственная сложность: O(1)
        """
        # TODO: реализовать проход справа налево
        pass


def run_tests():
    """Запуск тестов для проверки решения"""
    solution = Solution()
    
    # Тест 1: Базовый случай
    assert solution.lengthOfLastWord("Hello World") == 5, "Тест 1 провален"
    
    # Тест 2: Много пробелов в начале и конце
    assert solution.lengthOfLastWord("   fly me   to   the moon  ") == 4, "Тест 2 провален"
    
    # Тест 3: Одно слово
    assert solution.lengthOfLastWord("luffy") == 5, "Тест 3 провален"
    
    # Тест 4: Пробелы только в конце
    assert solution.lengthOfLastWord("joyboy   ") == 6, "Тест 4 провален"
    
    # Тест 5: Длинное слово
    assert solution.lengthOfLastWord("a") == 1, "Тест 5 провален"
    
    # Тест 6: Сложный пример
    assert solution.lengthOfLastWord("luffy is still joyboy") == 6, "Тест 6 провален"
    
    print("Все тесты пройдены!")


if __name__ == "__main__":
    run_tests()