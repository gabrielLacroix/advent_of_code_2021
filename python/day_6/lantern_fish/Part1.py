if __name__ == '__main__':
    data = open('input').read().split(',')
    data = [int(f) for f in data]

    for i in range(80):
        new_fish = []
        for fish_index, fish in enumerate(data):
            if fish == 0:
                new_fish.append(8)
                data[fish_index] = 6
            else:
                data[fish_index] = fish - 1
        data.extend(new_fish)

    print(len(data))
