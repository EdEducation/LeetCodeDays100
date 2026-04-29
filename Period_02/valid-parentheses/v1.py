# Задача: Valid Parentheses (Проверка валидности скобочной последовательности)
# 
# Известное решение: Использование стека (Stack)
# Сложность: O(n) по времени, O(n) в худшем случае по памяти
#
# Именованный алгоритм: Алгоритм проверки скобок с помощью стека
# (Matching Parentheses algorithm / Bracket validation algorithm)
#
# Примечание: Решение за O(1) невозможно, так как необходимо 
# обработать все символы строки длиной n, что как минимум O(n).

class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # если открывающая скобка - наполняем, иначе извлекаем последний элемент, должен быть парным к закрывающему
        mapping = {')':'(','}':'{',']':'['} # словарь парных элементов

        for char in s:
            if char in "({[": # открывающая скобка
                stack.append(char)
            else: # закрывающая скобка
                if not stack: # stack пуст
                    return False
                else:
                    top = stack.pop() # извлекаем последний элемент из stack
                    if top != mapping[char]:
                        return False
                    
        return len(stack) == 0 # stack в конце должен остаться пустым



# Тесты
def run_tests():
    solution = Solution()
    
    # Тест 1: Простые скобки
    assert solution.isValid("()") == True, "Тест 1 провален"
    
    # Тест 2: Несколько типов скобок
    assert solution.isValid("()[]{}") == True, "Тест 2 провален"
    
    # Тест 3: Неправильное закрытие
    assert solution.isValid("(]") == False, "Тест 3 провален"
    
    # Тест 4: Вложенные правильные скобки
    assert solution.isValid("([])") == True, "Тест 4 провален"
    
    # Тест 5: Неправильный порядок
    assert solution.isValid("([)]") == False, "Тест 5 провален"
    
    # Тест 6: Только открывающая скобка
    assert solution.isValid("(") == False, "Тест 6 провален"
    
    # Тест 7: Только закрывающая скобка
    assert solution.isValid("]") == False, "Тест 7 провален"
    
    # Тест 8: Пустая строка (хотя по условию длина >= 1)
    assert solution.isValid("") == True, "Тест 8 провален"
    
    # Тест 9: Длинная валидная последовательность
    assert solution.isValid("{[]}([{}])") == True, "Тест 9 провален"
    
    # Тест 10: Несоответствие типов
    assert solution.isValid("([)]") == False, "Тест 10 провален"
    
    print("Все тесты пройдены!")


# Запуск тестов
if __name__ == "__main__":
    run_tests()