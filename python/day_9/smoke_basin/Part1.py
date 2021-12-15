if __name__ == '__main__':
    data = open('input').read().split('\n')
    data.remove('')

    tab = [line for line in [[c for c in l] for l in data]]

    def get_up(x, y):
        if y == 0:
            return 1000
        return int(tab[x][y-1])

    def get_down(x, y):
        if y == 99:
            return 1000
        return int(tab[x][y+1])

    def get_left(x, y):
        if x == 0:
            return 1000
        return int(tab[x-1][y])

    def get_right(x, y):
        if x == 99:
            return 1000
        return int(tab[x+1][y])
    low_points = []
    for x in range(100):
        for y in range(100):
            value = int(tab[x][y])
            is_low_point = value < get_up(x, y) and value < get_down(x, y) and value < get_left(x, y) and value < get_right(x, y)
            if is_low_point:
                low_points.append(value)
    print(sum([int(v) + 1 for v in low_points]))
