if __name__ == '__main__':
    data = open('input').read().split('\n')
    data.remove('')

    def get_values(line):
        split = line.split()
        split.remove('->')
        values = []
        if is_horizontal(split):

            p1, p2 = split
            x1, y = p1.split(',')
            x2, _ = p2.split(',')
            x1, x2 = int(x1), int(x2)
            x1, x2 = min_max(x1, x2)
            for x in range(int(x1), int(x2) + 1):
                values.append((x, int(y)))
            pass
        elif is_vertical(split):
            p1, p2 = split
            x, y1 = p1.split(',')
            _, y2 = p2.split(',')
            y1, y2 = int(y1), int(y2)
            y1, y2 = min_max(y1, y2)
            for y in range(int(y1), int(y2) + 1):
                values.append((int(x), y))
            pass
        return values

    def min_max(a, b):
        if a < b:
            return a, b
        return b, a

    def is_vertical(line):
        p1, p2 = line
        x1, _ = p1.split(',')
        x2, _ = p2.split(',')

        return x1 == x2

    def is_horizontal(line):
        p1, p2 = line
        _, y1 = p1.split(',')
        _, y2 = p2.split(',')
        return y1 == y2

    list_of_2s = set()
    list_of_1s = set()

    for entry in data:
        values = get_values(entry)
        for point in values:
            if point in list_of_1s:
                list_of_2s.add(point)
            else:
                list_of_1s.add(point)

    print(len(list_of_2s))

