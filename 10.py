matrix = [[1, 2, 3, 4, 5, 6, 7, 8 ],
          [8, 7, 6, 5, 4, 3, 2, 1 ],
          [2, 3, 4, 5, 6, 7, 8, 9 ],
          [9, 8, 7, 6, 5, 4, 3, 2 ],
          [1, 3, 5, 7, 9, 7, 5, 3 ],
          [3, 1, 5, 3, 2, 6, 5, 7 ],
          [1, 7, 5, 9, 7, 3, 1, 5 ],
          [2, 6, 3, 5, 1, 7, 3, 2 ]]


def getAllInSquare(matrix):
    for row in matrix:
        for i in range(0,len(row)):
            row[i] = pow(row[i],2)
    return matrix

def getEvenInSquare(matrix):
    for row in matrix:
        for i in range(0,len(row)):
            if(row[i]%2 == 0):
                row[i] = pow(row[i],2)
    return matrix

print(getEvenInSquare(matrix))