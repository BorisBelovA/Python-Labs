import  random
def read_sudoku(filename):
    """ Прочитать Судоку из указанного файла """
    digits = [c for c in open(filename).read() if c in '123456789.']
    grid = group(digits, 9)
    return grid

def display(values):
    """Вывод Судоку """
    width = 2
    line = '+'.join(['-' * (width * 3)] * 3)
    for row in range(9):
        print(''.join(values[row][col].center(width) + ('|' if str(col) in '25' else '') for col in range(9)))
        if str(row) in '25':
            print(line)
    print()

def group(values, n):
    """Сгруппировать значения values в список, состоящий из списков по n элементов"""
    return [values[i:i+n] for i in range(0, len(values), n)]

def get_row(values, pos):
    """ Возвращает все значения для номера строки, указанной в pos """
    row, _ = pos
    return values[row]

def get_col(values, pos):
    """ Возвращает все значения для номера столбца, указанного в pos"""
    _, col = pos
    return [values[row][col] for row in range(len(values))]

def get_block(values, pos):
    """ Возвращает все значения из квадрата, в который попадает позиция pos"""
    row, col = pos
    br = 3 * (row // 3)
    #print(br)
    bc = 3 * (col // 3)
    #print(bc)
    return [values[br+r][bc+c] for r in range(3) for c in range(3)]

def find_empty_positions(grid):
    """ Найти первую свободную позицию в пазле"""
    for row in range(len(grid)):
        for col in range(len(grid)):
            if grid[row][col] == '.':
                return (row, col)
    return None

def find_possible_values(grid, pos):
    """ Вернуть множество возможных значения для указанной позиции"""
    return set('123456789') - set(get_row(grid, pos)) - set(get_col(grid, pos)) - set(get_block(grid, pos))

def solve(grid):
    """ Решение пазла, заданного в grid """
    pos = find_empty_positions(grid)
    if not pos:
        return grid
    row, col = pos
    for value in find_possible_values(grid, pos):
        grid[row][col] = value
        solution = solve(grid)
        if solution:
            return solution
    grid[row][col] = '.'
    return None

def check_solution(solution):
    """ Если решение solution верно, то вернуть True, в противном случае False """
    for row in range(len(solution)):
        row_values = set(get_row(solution, (row, 0)))
        if row_values != set('123456789'):
            return False

    for col in range(len(solution)):
        col_values = set(get_col(solution, (0, col)))
        if col_values != set('123456789'):
            return False

    for row in (0, 3, 6):
        for col in (0, 3, 6):
            blk_values = set(get_block(solution, (row, col)))
            if blk_values != set('123456789'):
                return False

    return True

def generate_sudoku(N):
    grid = solve([['.']*9 for _ in range(9)])
    N = 81 - min(81, max(0,N))

    while N:
        row = random.randint(0,8)
        col = random.randint(0,8)
        if(grid[row][col] != '.'):
            grid[row][col] = '.'
            N-=1
    return grid

if __name__ == '__main__':

    grid = read_sudoku('grid.txt')
    display(grid)
    solution = solve(grid)
    display(solution)
    print(check_solution(solution))
    print(generate_sudoku(48))