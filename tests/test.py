import numpy as np

h = 10
w = 10
pm_width = 10
pm_height = 10

A = [[col for col in range(w + 1)] for row in range(h)]
map_index = np.array(A)
# print(map_index)

pm = [[1.00 for j in range(w)] for i in range(h)]

h = 10
w = 10
rm = [[-1.00 for k in range(w)] for g in range(h)]


def generate_move_map(x, y, moves=3):

    if rm[x][y] < float(moves):
        rm[x][y] = float(moves)
        for _x in range(-1, 2):  # Проходит циклом вокруг центра
            for _y in range(-1, 2):
                if (_x, _y) != (0, 0):
                    nX = _x + x
                    nY = _y + y
                    if 0 <= nX < w and 0 <= nY < h:  # w = 10, h = 10
                        if abs(_x) + abs(_y) == 2:
                            move_weight = 1.5
                        else:
                            move_weight = 1
                        t = moves - move_weight * pm[nX][nY]
                        if t >= 0:
                            generate_move_map(nX, nY, t)
                _y += 1
            _x += 1


generate_move_map(5, 5)

for f in rm:
    print(f)
