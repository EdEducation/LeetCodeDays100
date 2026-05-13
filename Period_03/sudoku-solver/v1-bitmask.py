from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Решение судоку с backtracking и битовыми масками для O(1) проверки
        """
        # Инициализация битовых масок
        self.rows = [0] * 9      # 9 строк
        self.cols = [0] * 9      # 9 столбцов
        self.boxes = [0] * 9     # 9 блоков 3x3
        
        # Заполнение масок на основе начальной доски
        for row in range(9):
            for col in range(9):
                if board[row][col] != '.':
                    num = int(board[row][col])
                    self.place_number(row, col, num)
        
        # Запуск рекурсивного поиска
        self.solve(board, 0, 0)
    
    def place_number(self, row: int, col: int, num: int) -> None:
        """
        Устанавливает число в маски (бит num-1)
        """
        bit = 1 << (num - 1)
        self.rows[row] |= bit
        self.cols[col] |= bit
        box_idx = (row // 3) * 3 + (col // 3)
        self.boxes[box_idx] |= bit
    
    def remove_number(self, row: int, col: int, num: int) -> None:
        """
        Удаляет число из масок
        """
        bit = 1 << (num - 1)
        self.rows[row] &= ~bit
        self.cols[col] &= ~bit
        box_idx = (row // 3) * 3 + (col // 3)
        self.boxes[box_idx] &= ~bit
    
    def is_valid(self, row: int, col: int, num: int) -> bool:
        """
        Проверяет, можно ли поставить число, используя битовые маски O(1)
        """
        bit = 1 << (num - 1)
        box_idx = (row // 3) * 3 + (col // 3)
        
        # Проверка за O(1) - просто проверяем биты
        return not (self.rows[row] & bit or 
                   self.cols[col] & bit or 
                   self.boxes[box_idx] & bit)
    
    def get_candidates(self, row: int, col: int) -> List[int]:
        """
        Возвращает список возможных чисел для клетки (оптимизация)
        """
        box_idx = (row // 3) * 3 + (col // 3)
        used = self.rows[row] | self.cols[col] | self.boxes[box_idx]
        
        candidates = []
        for num in range(1, 10):
            bit = 1 << (num - 1)
            if not (used & bit):
                candidates.append(num)
        
        return candidates
    
    def find_best_cell(self, board: List[List[str]]) -> tuple:
        """
        Находит клетку с минимальным количеством вариантов (MRV эвристика)
        Возвращает (row, col, candidates) или (None, None, None) если нет пустых
        """
        best_row = best_col = None
        best_candidates = None
        min_candidates = 10
        
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    candidates = self.get_candidates(row, col)
                    if len(candidates) < min_candidates:
                        min_candidates = len(candidates)
                        best_row, best_col = row, col
                        best_candidates = candidates
                        if min_candidates == 1:  # Ранний выход
                            return best_row, best_col, best_candidates
        
        return best_row, best_col, best_candidates
    
    def solve(self, board: List[List[str]], row: int = 0, col: int = 0) -> bool:
        """
        Рекурсивный поиск с возвратом и MRV эвристикой
        """
        # Находим лучшую клетку для заполнения (MRV эвристика)
        row, col, candidates = self.find_best_cell(board)
        
        # Если пустых клеток нет - судоку решена
        if row is None:
            return True
        
        # Пробуем все варианты для выбранной клетки
        for num in candidates:
            if self.is_valid(row, col, num):
                # Ставим число
                board[row][col] = str(num)
                self.place_number(row, col, num)
                
                # Рекурсивно решаем дальше
                if self.solve(board):
                    return True
                
                # Откатываем изменения (backtrack)
                board[row][col] = '.'
                self.remove_number(row, col, num)
        
        return False


# Альтернативная версия с использованием множеств (hash sets) - более понятная для начинающих
class SolutionWithSets:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Решение судоку с использованием множеств для O(1) проверки
        """
        # Инициализация множеств
        self.rows = [set() for _ in range(9)]
        self.cols = [set() for _ in range(9)]
        self.boxes = [set() for _ in range(9)]
        
        # Заполнение множеств на основе начальной доски
        for row in range(9):
            for col in range(9):
                if board[row][col] != '.':
                    num = board[row][col]
                    self.rows[row].add(num)
                    self.cols[col].add(num)
                    box_idx = (row // 3) * 3 + (col // 3)
                    self.boxes[box_idx].add(num)
        
        # Запуск рекурсивного поиска
        self.solve(board)
    
    def is_valid(self, row: int, col: int, num: str) -> bool:
        """
        Проверка за O(1) через множества
        """
        box_idx = (row // 3) * 3 + (col // 3)
        return (num not in self.rows[row] and 
                num not in self.cols[col] and 
                num not in self.boxes[box_idx])
    
    def place_number(self, row: int, col: int, num: str) -> None:
        """
        Добавление числа в множества
        """
        box_idx = (row // 3) * 3 + (col // 3)
        self.rows[row].add(num)
        self.cols[col].add(num)
        self.boxes[box_idx].add(num)
    
    def remove_number(self, row: int, col: int, num: str) -> None:
        """
        Удаление числа из множеств
        """
        box_idx = (row // 3) * 3 + (col // 3)
        self.rows[row].remove(num)
        self.cols[col].remove(num)
        self.boxes[box_idx].remove(num)
    
    def find_empty(self, board: List[List[str]]) -> tuple:
        """
        Находит первую пустую клетку (можно улучшить с MRV)
        """
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    return row, col
        return None, None
    
    def solve(self, board: List[List[str]]) -> bool:
        """
        Рекурсивный поиск с возвратом
        """
        row, col = self.find_empty(board)
        
        # Если пустых клеток нет - судоку решена
        if row is None:
            return True
        
        # Пробуем все цифры от 1 до 9
        for num in map(str, range(1, 10)):
            if self.is_valid(row, col, num):
                # Ставим число
                board[row][col] = num
                self.place_number(row, col, num)
                
                # Рекурсивно решаем дальше
                if self.solve(board):
                    return True
                
                # Откатываем изменения (backtrack)
                board[row][col] = '.'
                self.remove_number(row, col, num)
        
        return False


# Тесты
def run_tests():
    # Тестируем битовые маски
    solution_bitmask = Solution()
    
    board1 = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    expected = [
        ["5","3","4","6","7","8","9","1","2"],
        ["6","7","2","1","9","5","3","4","8"],
        ["1","9","8","3","4","2","5","6","7"],
        ["8","5","9","7","6","1","4","2","3"],
        ["4","2","6","8","5","3","7","9","1"],
        ["7","1","3","9","2","4","8","5","6"],
        ["9","6","1","5","3","7","2","8","4"],
        ["2","8","7","4","1","9","6","3","5"],
        ["3","4","5","2","8","6","1","7","9"]
    ]
    
    solution_bitmask.solveSudoku(board1)
    assert board1 == expected, "Тест 1 (битовые маски) провален"
    print("✓ Тест 1 с битовыми масками пройден")
    
    # Тестируем множества
    solution_sets = SolutionWithSets()
    board2 = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    
    solution_sets.solveSudoku(board2)
    assert board2 == expected, "Тест 2 (множества) провален"
    print("✓ Тест 2 с множествами пройден")
    
    print("\n✅ Все тесты пройдены!")


if __name__ == "__main__":
    run_tests()