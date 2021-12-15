if __name__ == '__main__':
    data = open('input').read().split(',')
    data = [int(f) for f in data]

    fishes = []
    for i in range(9):
        fishes.append(data.count(i))

    for day in range(256):
        new_fishes = fishes.copy()
        new_fishes[8] = fishes[0]
        new_fishes[7] = fishes[8]
        new_fishes[6] = fishes[7] + fishes[0]
        new_fishes[5] = fishes[6]
        new_fishes[4] = fishes[5]
        new_fishes[3] = fishes[4]
        new_fishes[2] = fishes[3]
        new_fishes[1] = fishes[2]
        new_fishes[0] = fishes[1]
        fishes = new_fishes

    total = fishes[0] + fishes[8] + fishes[7] + fishes[6] + fishes[5] + fishes[4] + fishes[3] + fishes[2] + fishes[1]
    print(total)
