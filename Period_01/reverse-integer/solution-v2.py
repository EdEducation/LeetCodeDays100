#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Задача: Reverse Integer (LeetCode 7)

Дано 32-битное знаковое целое число x. Верните число x с переставленными в обратном порядке цифрами.
Если при перевороте число выходит за пределы 32-битного знакового целочисленного диапазона [-2^31, 2^31 - 1],
то верните 0.

Предполагается, что среда выполнения НЕ позволяет хранить 64-битные целые числа (ни знаковые, ни беззнаковые).

Примеры:
- Вход: x = 123    -> Выход: 321
- Вход: x = -123   -> Выход: -321
- Вход: x = 120    -> Выход: 21

Ограничения:
- -2^31 <= x <= 2^31 - 1

Примечание:
- Ведущие нули в перевёрнутом числе отбрасываются (как в примере с 120 -> 21).
- Для Python, где целые числа не ограничены по размеру, необходимо самостоятельно эмулировать 32-битное переполнение.
"""

from termcolor import colored


class Solution:
    # Справочник граничных значений для 32-битного signed int
    INT32_LIMITS = {
        'min': -2147483648,
        'max': 2147483647,
        'max_abs': 2147483647
    }
    
    def reverse(self, x: int) -> int:
        INT_MIN = self.INT32_LIMITS['min']
        INT_MAX = self.INT32_LIMITS['max']
        
        # Сохраняем знак числа
        if x < 0:
            sign = -1
            x_str = str(-x)  # Работаем с абсолютным значением
        else:
            sign = 1
            x_str = str(x)
        
        # Переворачиваем строку
        reversed_str = x_str[::-1]
        
        # Удаляем лидирующие нули (преобразование в int автоматически удалит их,
        # но мы сначала проверяем, не пустая ли строка)
        if not reversed_str:  # Если строка пустая (x = 0)
            reversed_num = 0
        else:
            reversed_num = int(reversed_str)
        
        # Восстанавливаем знак
        result = sign * reversed_num
        
        # Проверяем 32-битное переполнение
        if result < INT_MIN or result > INT_MAX:
            return 0
            
        return result


# Тесты
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        (123, 321),
        (-123, -321),
        (120, 21),
        (0, 0),
        (1534236469, 0),  # Переполнение
        (-2147483648, 0),  # Переполнение
        (1463847412, 2147483641),  # Максимальное возможное
        (2147483647, 0),  # Переполнение
        (-2147483412, -2143847412),  # Работает в границах
    ]
    
    print("Запуск тестов для reverse integer (строковое решение):")
    print("-" * 50)
    
    passed = 0
    for i, (input_val, expected) in enumerate(test_cases, 1):
        result = solution.reverse(input_val)
        console_color = "green"

        if result == expected:
            status = "✓"
        else:
            status = "✗"
            console_color = "red"

        
        print(colored(f"Тест {i}: {status}", console_color))
        print(f"  Вход: {input_val}")
        print(f"  Ожидалось: {expected}")
        print(f"  Получено: {result}")
        print()
        if result == expected:
            passed += 1
    
    print("-" * 50)
    print(f"Результат: {passed}/{len(test_cases)} тестов пройдено")