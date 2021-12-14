def count_increases(val):
    count = 0
    for x in range(1, len(val)):
        if val[x] - val[x - 1] > 0:
            # print(data[x] + " is bigger than " + data[x - 1])
            count += 1
    print(count)


def sanitize_input(source):
    val = []
    for x in range(len(source)):
        if source[x].isnumeric():
            val.append(int(source[x]))
    return val


if __name__ == '__main__':
    data = open('input').read().split('\n')

    values = sanitize_input(data)
    count_increases(values)
