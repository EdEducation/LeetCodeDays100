class Solution:
    def countAndSay(self, n: int) -> str:
        """
        Возвращает n-й элемент последовательности count-and-say.
        
        Алгоритм:
        - Начинаем с "1"
        - Для каждого шага от 2 до n применяем RLE к предыдущей строке
        - RLE: группируем одинаковые подряд идущие символы,
                записываем "количество" + "символ"
        
        Временная сложность: O(2^n) для n ≤ 30
        Пространственная сложность: O(2^n)
        """
        if n == 1:
            return "1"
        
        result = "1"
        
        for _ in range(2, n + 1):
            chars = []
            count = 1
            prev = result[0]
            
            for curr in result[1:]:
                if curr == prev:
                    count += 1
                else:
                    chars.append(str(count))
                    chars.append(prev)
                    prev = curr
                    count = 1
            
            # Добавляем последнюю группу
            chars.append(str(count))
            chars.append(prev)
            
            result = ''.join(chars)
        
        return result
            


def run_tests():
    """Запуск тестов для проверки решения"""
    solution = Solution()
    
    # Базовый тест
    assert solution.countAndSay(1) == "1", "Тест 1 провален"
    assert solution.countAndSay(2) == "11", "Тест 2 провален"
    assert solution.countAndSay(3) == "21", "Тест 3 провален"
    assert solution.countAndSay(4) == "1211", "Тест 4 провален"
    assert solution.countAndSay(5) == "111221", "Тест 5 провален"
    assert solution.countAndSay(6) == "312211", "Тест 6 провален"
    
    # Дополнительные тесты из условий задачи
    assert solution.countAndSay(1) == "1", "Тест n=1 провален"
    assert solution.countAndSay(4) == "1211", "Тест n=4 провален"
    
    # Граничный тест
    assert len(solution.countAndSay(30)) > 0, "Тест n=30 провален"
    
    print("Все тесты пройдены успешно!")


if __name__ == "__main__":
    run_tests()