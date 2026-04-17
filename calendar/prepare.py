class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # реализовать
        pass


# Тесты
def run_tests():
    solution = Solution()
    
    # Тест 1: Базовый пример без переноса
    assert solution.plusOne([1, 2, 3]) == [1, 2, 4], "Тест 1 провален"
    
    print("Все тесты пройдены!")


# Запуск тестов
if __name__ == "__main__":
    run_tests()