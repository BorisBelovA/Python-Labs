import pygame
from pygame.locals import *
import random


class GameOfLife:
    def __init__(self, width=640, height=480, cell_size=10, speed=10):
        self.width = width
        self.height = height
        self.cell_size = cell_size

        # Устанавливаем размер окна
        self.screen_size = width, height
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)

        # Вычисляем количество ячеек по вертикали и горизонтали
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        # Скорость протекания игры
        self.speed = speed

    def run(self):
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))
        running = True

        rects = game.cell_list(randomize=True)

        #print(rects)

        self.draw_cell_list(rects)

        rects = self.update_cell_list(rects)

        #self.draw_cell_list(rects)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.draw_cell_list(rects)
            rects = self.update_cell_list(rects)
            self.draw_grid()
            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()

    def draw_grid(self):
        # http://www.pygame.org/docs/ref/draw.html#pygame.draw.line
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                             (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'), (0, y), (self.width, y))

    def cell_list(self, randomize=False):
        """
        Создание списка клеток.
        Клетка считается живой, если ее значение равно 1.
        В противном случае клетка считается мертвой, то
        есть ее значение равно 0.
        Если параметр randomize = True, то создается список, где
        каждая клетка может быть равновероятно живой или мертвой.
        """
        #self.cell_height - row
        #self.cell_width - col
        list = [[random.randint(0,1) for _ in range(self.cell_height)] for i in range(self.cell_width)]
        return list

    def draw_cell_list(self, rects):
        """
        Отображение списка клеток 'rects' с закрашиванием их в
        соответствующе цвета
        """
        #pygame.draw.rect(self.screen, pygame.Color('green'), rects)
        for i in range(len(rects)):
            for j in range(len(rects[i])):
                if(rects[i][j]==1):
                    pygame.draw.rect(self.screen, pygame.Color('green'),
                                   [i*self.cell_size, j*self.cell_size, self.cell_size, self.cell_size])
                else:
                    pygame.draw.rect(self.screen, pygame.Color('white'),
                                    [i * self.cell_size, j * self.cell_size, self.cell_size, self.cell_size])


    def get_neighbours(self, cell):
        """
        Вернуть список соседних клеток для клетки cell.

        Соседними считаются клетки по горизонтали,
        вертикали и диагоналям, то есть во всех
        направлениях.
        """
        # cell = list[i][j]
        # Столбец Строка
        x = cell[0]
        y = cell[1]
        '''neighbours = [(x + i * self.cell_size, y + i * self.cell_size) for i in range(-1, 2) for j in range(-1, 2) if
                      not i == j == 0]'''
        #neighbours = []
        #neighbours.append([[x-1,y-1], [x-1,y], [x-1,y+1], [x, y-1], [x,y+1], [x+1,y-1],[x+1,y],[x+1,y+1]])
        #[-1,-1] [-1,0] [0,-1]
        neighbours = [(x + i, y+j) for i in range(-1,2) for j in range(-1,2) if not i == j == 0]
        index = []
        for elem in neighbours:
            if ((elem[0] < 0) or (elem[1] < 0)):
                index.append(neighbours.index(elem))

        index.reverse()
        for i in index:
            del neighbours[i]
        #print(x, '   ', y)
        return neighbours


    def update_cell_list(self, cell_list):
        """
        Обновление состояния клеток
        [Столбец][Строка]
        """
        for i in range(len(cell_list)-1):
            for j in range(len(cell_list[i])-1):
                neighbours = self.get_neighbours([i,j])
                count = 0
                for elem in neighbours:
                    if(cell_list[elem[0]][elem[1]] == 1):
                        count+=1
                if 2<=count<=3:
                    cell_list[i][j] = 1
                else:
                    cell_list[i][j] = 0
                #print( 'neighbours: ',neighbours,'   ', len(neighbours), ' Count  ', count)

        '''neighbours = self.get_neighbours([0, 0])
        print('cell ', [0,0], 'neighbours: ',neighbours)
        
        count = 0
        for elem in neighbours:
            if (cell_list[elem[0]][elem[1]] == 1):
                count += 1
                print(elem, ' Сосед' )
        print(count)'''

        #print('Updated list: ',cell_list)
        return cell_list

if __name__ == '__main__':
    game = GameOfLife(320, 240, 20)
    game.run()

