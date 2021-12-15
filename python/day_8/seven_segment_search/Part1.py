if __name__ == '__main__':
    data = open('input').read().split('\n')
    data.remove('')

    valid_digits = [2, 3, 4, 7]
    count = 0
    for entry in data:
        pipe = entry.index('|')
        entry = entry[pipe+1:]
        digits = entry.split()
        for digit in digits:
            if len(digit) in valid_digits:
                count += 1
    print(count)