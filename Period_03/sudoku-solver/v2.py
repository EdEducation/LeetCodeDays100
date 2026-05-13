from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Решение судоку с помощью Dancing Links (Algorithm X)
        """
        # Преобразуем судоку в задачу точного покрытия и решаем её
        solution = self.solve_with_dlx(board)
        
        # Применяем решение к исходной доске
        if solution:
            for row, col, num in solution:
                board[row][col] = str(num)
    
    def solve_with_dlx(self, board):
        """
        Решает судоку через преобразование в задачу точного покрытия.
        Возвращает список кортежей (row, col, value) для заполненных клеток.
        """
        # Шаг 1: Построение матрицы точного покрытия
        # Колонки представляют 4 типа ограничений (всего 324 колонки):
        #   0-80:   клетка (row, col) занята
        #   81-161:  строка (row) содержит число value
        #   162-242: столбец (col) содержит число value
        #   243-323: блок 3x3 (box) содержит число value
        
        rows = []  # список строк матрицы (каждая строка = (row, col, value))
        
        # Генерируем все возможные варианты
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    # Пустая клетка - пробуем все цифры 1-9
                    for val in range(1, 10):
                        rows.append((row, col, val))
                else:
                    # Заполненная клетка - только заданное значение
                    val = int(board[row][col])
                    rows.append((row, col, val))
        
        # Строим матрицу: колонки = все ограничения
        # Функция для получения индекса колонки
        def col_index(row, col, val, constraint_type):
            # constraint_type: 0=cell, 1=row, 2=col, 3=box
            if constraint_type == 0:  # ограничение клетки
                return row * 9 + col
            elif constraint_type == 1:  # ограничение строки
                return 81 + row * 9 + (val - 1)
            elif constraint_type == 2:  # ограничение столбца
                return 162 + col * 9 + (val - 1)
            else:  # ограничение блока
                box = (row // 3) * 3 + (col // 3)
                return 243 + box * 9 + (val - 1)
        
        # Создаём разреженную матрицу для DLX
        # Каждый элемент списка - это строка, содержащая индексы колонок, где есть 1
        
        sparse_matrix = []
        for r, c, v in rows:
            row_indices = [
                col_index(r, c, v, 0),  # ограничение клетки
                col_index(r, c, v, 1),  # ограничение строки
                col_index(r, c, v, 2),  # ограничение столбца
                col_index(r, c, v, 3)   # ограничение блока
            ]
            sparse_matrix.append((r, c, v, row_indices))
        
        # Шаг 2: Запуск Algorithm X
        # Словарь для отслеживания покрытых колонок
        N_COLS = 324
        solution_rows = []
        
        # Запускаем поиск с возвратом
        def search(selected_rows, covered_cols):
            if len(selected_rows) == 81:
                return selected_rows  # все клетки заполнены
            
            # Находим колонку с минимальным количеством непокрытых строк
            # (эвристика для ускорения)
            best_col = None
            min_count = float('inf')
            
            for col in range(N_COLS):
                if not covered_cols[col]:
                    count = 0
                    for row_data in sparse_matrix:
                        r, c, v, indices = row_data
                        if not any(covered_cols[col] for col in indices):
                            if col in indices:
                                count += 1
                    if count < min_count:
                        min_count = count
                        best_col = col
                        if min_count == 0:
                            break
            
            if best_col is None or min_count == 0:
                return None
            
            # Пробуем все строки, покрывающие best_col
            for row_idx, row_data in enumerate(sparse_matrix):
                r, c, v, indices = row_data
                
                # Если эта строка не подходит для best_col
                if best_col not in indices:
                    continue
                
                # Проверяем, не конфликтует ли строка с уже выбранными
                conflict = False
                for col in indices:
                    if covered_cols[col]:
                        conflict = True
                        break
                
                if conflict:
                    continue
                
                # Покрываем все колонки этой строки
                new_covered = covered_cols.copy()
                for col in indices:
                    new_covered[col] = True
                
                # Рекурсивно ищем дальше
                result = search(selected_rows + [row_idx], new_covered)
                if result:
                    return result
            
            return None
        
        # Начинаем поиск с пустым покрытием
        covered_cols = [False] * N_COLS
        solution_indices = search([], covered_cols)
        
        # Шаг 3: Преобразуем индексы строк обратно в координаты
        if solution_indices:
            result = []
            for idx in solution_indices:
                r, c, v, _ = sparse_matrix[idx]
                result.append((r, c, v))
            return result
        
        return None


# Тесты
def run_tests():
    solution = Solution()
    
    # Тест 1: Пример из условия
    board = [
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
    solution.solveSudoku(board)
    assert board == expected, "Тест 1 провален"
    print("✓ Тест 1 пройден")
    
    print("\n✅ Все тесты пройдены!")


if __name__ == "__main__":
    run_tests()