import random
def read_sudoku(filename):
    """ Прочитать Судоку из указанного файла """
    digits = [c for c in open(filename).read() if c in '123456789.']
    grid = group(digits, 9)
    return grid

def group(values, n):
    """
    Сгруппировать значения values в список, состоящий из списков по n элементов
    group([1,2,3,4], 2)
    [[1, 2], [3, 4]]
    group([1,2,3,4,5,6,7,8,9], 3)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """
    # PUT YOUR CODE HERE
    '''row = values[0:2]
    row = values[2:4]
    row = values[4:6]'''
    grid = []
    start = 0
    end = n
    while end <= len(values):
        grid.append(values[start: end:])
        start = end
        end += n
        #print(grid,'  ', end)
    return grid

def display(values):
    """Вывод Судоку """
    width = 2
    line = '+'.join(['-' * (width * 3)] * 3)
    for row in range(9):
        print(''.join(values[row][col].center(width) + ('|' if str(col) in '25' else '') for col in range(9)))
        if str(row) in '25':
            print(line)

#group([1,3,4,5,6,8],3)

def get_row(values, pos):
    row = values[pos]
    return row

def get_col(values,pos):
    col = []
    for i in range(len(values)):
        col.append(values[i][pos])
    return col

def get_block(values, pos):
    block = []
    length = 3
    index_arr = [i for i in range(len(values))]
    temp_arr = []
    i = 0
    while i < len(values):
        temp_arr.append(index_arr[i:i+length:1])
        i+=length
    index_arr = temp_arr
    for i in range(len(index_arr)):
        for j in range(len(index_arr[i])):
            if(index_arr[i][j] == pos[0]):
                row_index = i              #Индекс строки
            if (index_arr[i][j] == pos[1]):
                col_index = i               #Индекс столбца
    for i in index_arr[row_index]:
        for j in index_arr[col_index]:
            block.append(grid[i][j])
    return block

def find_empty_positions(grid):
    for i in range(len(grid)):
        row = get_row(grid, i)
        try:
            index = row.index('.')
            break
        except ValueError:
            index = -1
    return [i, index]

def find_possible_values(grid, pos):
    pos_row = pos[0]
    pos_col = pos[1]
    values = {i for i in range(10)} # {0,1,2,3,4,5,6,7,8,9}
    values.remove(0) #Удялем 0 из списка

    values_row = set(get_row(grid, pos_row)) # Создаем множество символьных элементов из строки
    values_row.discard('.') # Удаляем '.'
    values_row = {int(elem) for elem in values_row} # Делаем это множество численным
    values.difference_update(values_row)

    #То же самое для столбца на заданной позиции
    values_col = set(get_col(grid, pos_col))
    values_col.discard('.')
    values_col = {int(elem) for elem in values_col}
    values.difference_update(values_col)

    values_block = set(get_block(grid, pos))
    values_block.discard('.')
    values_block = {int(elem) for elem in values_block}
    values.difference_update(values_block)
    return values


def solve(grid):
    """ Решение пазла, заданного в grid """
    """ Как решать Судоку?
        1. Найти свободную позицию
        2. Найти все возможные значения, которые могут находиться на этой позиции
        3. Для каждого возможного значения:
            3.1. Поместить это значение на эту позицию
            3.2. Продолжить решать оставшуюся часть пазла
    >>> grid = read_sudoku('puzzle1.txt')
    >>> solve(grid)
    [['5', '3', '4', '6', '7', '8', '9', '1', '2'], ['6', '7', '2', '1', '9', '5', '3', '4', '8'], ['1', '9', '8', '3', '4', '2', '5', '6', '7'], ['8', '5', '9', '7', '6', '1', '4', '2', '3'], ['4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', '9', '2', '4', '8', '5', '6'], ['9', '6', '1', '5', '3', '7', '2', '8', '4'], ['2', '8', '7', '4', '1', '9', '6', '3', '5'], ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
    """
    pos = find_empty_positions(grid)
    #print(pos)
    if not pos:
        return grid
    row, col = pos
    #print(find_possible_values(grid,pos))
    for value in find_possible_values(grid, pos):
        grid[row][col] = value
        solution = solve(grid)
        #print(solve(grid))
        if solution:
            return solution
    grid[row][col] = '.'
    return None





if __name__ == '__main__':
    grid = read_sudoku('grid.txt')
    display(grid)
    solution = solve(grid)
    display(solution)

#solve(grid)


#print(get_row(grid,0))
#print(get_col(grid,0))
#block_length = len(get_block(grid,(4,3)))
#print(get_block(grid,(4,3)))

#print(find_empty_positions(grid))
#row = get_row(grid,0)




