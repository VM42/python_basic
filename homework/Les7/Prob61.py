class Matrix:
    def __init__(self, list_x, list_y):
        self.list_x = list_x
        self.list_y = list_y

    def __add__(self):
        neo = [[0, 0, 0],
               [0, 0, 0],
               [0, 0, 0]]

        for y in range(len(self.list_x)):
            for u in range(len(self.list_y[y])):
                neo[y][u] = self.list_x[y][u] + self.list_y[y][u]

        return str('\n'.join(['\t'.join([str(u) for u in y]) for y in neo]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(u) for u in y]) for y in neo]))
# had to google how to make matrix, tho it still show unresolved ref in __str__


trinity = Matrix([[2, 59, 11],
                  [1, 1, -1],
                  [41, 16, 2]],
                 [[40, 10, 10],
                  [3, 1, 1],
                  [-40, -12, 6]])


print(trinity.__add__())
