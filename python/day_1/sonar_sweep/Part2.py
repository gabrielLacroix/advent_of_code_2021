from day_1.sonar_sweep.SonarSweep import count_increases, sanitize_input

if __name__ == '__main__':
    data = open('input').read().split('\n')

    values = sanitize_input(data)

    windows = []
    for x in range(2, len(values)):
        windows.append(int(data[x - 2]) + int(data[x - 1]) + int(data[x]))

    count_increases(windows)