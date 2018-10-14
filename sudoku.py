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

#A function to check if the grid is full
def checkGrid(grid):
  for row in range(0,9):
      for col in range(0,9):
        if grid[row][col]==0:
          return False

  #We have a complete grid!
  return True

def solve(grid):
    """ Решение пазла, заданного в grid

    Как решать Судоку?
        1. Найти свободную позицию
        2. Найти все возможные значения, которые могут находиться на этой позиции
        3. Для каждого возможного значения:
            3.1. Поместить это значение на эту позицию
            3.2. Продолжить решать оставшуюся часть пазла

    grid = read_sudoku('puzzle1.txt')
    solve(grid)"""
    # PUT YOUR CODE HERE
    #while find_empty_positions(grid)[1] != -1:
    '''try:
        empty_pos = find_empty_positions(grid)
        possible_values = find_possible_values(grid, empty_pos)
        index = random.randint(0, len(possible_values) - 1)
        i = 0
        for elem in possible_values:
            if (i == index):
                element = elem
                break
            i += 1
        grid[empty_pos[0]][empty_pos[1]] = str(element)
        roolback_dict[elem] = (empty_pos)
        print(roolback_dict)
    except ValueError:
        solve(grid)
    return  grid'''
    # Find next empty cell
    for i in range(0, 81):
        row = i // 9
        col = i % 9
        display(grid)
        print('/////////////////////')
        if grid[row][col] == 0:
            for value in range(1, 10):
                # Check that this value has not already be used on this row
                if not (value in grid[row]):
                    # Check that this value has not already be used on this column
                    if not value in (
                    grid[0][col], grid[1][col], grid[2][col], grid[3][col], grid[4][col], grid[5][col], grid[6][col],
                    grid[7][col], grid[8][col]):
                        # Identify which of the 9 squares we are working on
                        square = []
                        if row < 3:
                            if col < 3:
                                square = [grid[i][0:3] for i in range(0, 3)]
                            elif col < 6:
                                square = [grid[i][3:6] for i in range(0, 3)]
                            else:
                                square = [grid[i][6:9] for i in range(0, 3)]
                        elif row < 6:
                            if col < 3:
                                square = [grid[i][0:3] for i in range(3, 6)]
                            elif col < 6:
                                square = [grid[i][3:6] for i in range(3, 6)]
                            else:
                                square = [grid[i][6:9] for i in range(3, 6)]
                        else:
                            if col < 3:
                                square = [grid[i][0:3] for i in range(6, 9)]
                            elif col < 6:
                                square = [grid[i][3:6] for i in range(6, 9)]
                            else:
                                square = [grid[i][6:9] for i in range(6, 9)]
                        # Check that this value has not already be used on this 3x3 square
                        if not value in (square[0] + square[1] + square[2]):
                            grid[row][col] = value
                            if checkGrid(grid):
                                print("Grid Complete and Checked")
                                return True
                            else:
                                if solve(grid):
                                    return True
            break
    print("Backtrack")
    grid[row][col] = 0


grid = read_sudoku('grid.txt')
solve(grid)


#print(get_row(grid,0))
#print(get_col(grid,0))
#block_length = len(get_block(grid,(4,3)))
#print(get_block(grid,(4,3)))

#print(find_empty_positions(grid))
#row = get_row(grid,0)




