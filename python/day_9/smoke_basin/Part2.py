if __name__ == '__main__':
    data = open('input').read().split('\n')
    data.remove('')

    tab = [line for line in [[int(c) for c in l] for l in data]]

    x = y = 0
    delimiters = [-1, 9]

    def find_next_basin():
        global x, y
        while tab[x][y] in delimiters:
            if x == 99:
                x = 0
                if y == 99:
                    return -1, -1
                y += 1
            else:
                x += 1
        return x, y

    def bleed_count(i, j):
        if i == -1 or i == 100 or j == -1 or j == 100:
            return 0
        if tab[i][j] in delimiters:
            return 0
        tab[i][j] = -1

        return 1 + bleed_count(i + 1, j) + bleed_count(i - 1, j) + bleed_count(i, j + 1) + bleed_count(i, j - 1)

    basins = []
    x_iter, y_iter = find_next_basin()
    while x_iter != -1:
        basins.append(bleed_count(x_iter, y_iter))
        x_iter, y_iter = find_next_basin()

    basins.sort()
    basins.reverse()
    print(basins[0] * basins[1] * basins[2])
