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
    #sgkddgg
    return True

grid = read_sudoku('grid.txt')
'''for arr in grid:
    print(arr)'''
display(grid)

