if __name__ == '__main__':
    data = open('input').read().split(',')
    data = [int(f) for f in data]

    fuel_counts = []
    for possible_index in range(max(data)):
        fuel_count = 0
        for crab in data:
            fuel_count += abs(crab - possible_index)
        fuel_counts.append(fuel_count)
    print(min(fuel_counts))