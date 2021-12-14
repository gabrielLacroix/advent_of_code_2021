
if __name__ == '__main__':
    data = open('input').read().split('\n')
    count = 0
    for x in range(1, len(data)):
        try:
            if int(data[x]) - int(data[x - 1]) > 0:
                # print(data[x] + " is bigger than " + data[x - 1])
                count += 1
        except ValueError:
            pass

    print(count)
