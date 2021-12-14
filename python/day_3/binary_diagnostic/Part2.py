if __name__ == '__main__':
    data = open('input').read().split('\n')

    number_of_bits = len(data[0])
    data.remove('')

    def filter(bit_val, bit_pos, source):
        result = []
        for value in source:
            if value[bit_pos] == str(bit_val):
                result.append(value)
        return result

    def most_common_bit(bit_pos, source):
        result = 0
        for value in source:
            result += int(value[bit_pos])
        return 1 if result >= len(source)/2 else 0

    def least_common_bit(bit_pos, source):
        return most_common_bit(bit_pos, source) ^ 1

    ogr_data = data
    c02sr = data
    for i in range(number_of_bits):
        bit = most_common_bit(i, ogr_data)
        ogr_data = filter(bit, i, ogr_data)
        if len(ogr_data) == 1:
            break

    for i in range(number_of_bits):
        bit = least_common_bit(i, c02sr)
        c02sr = filter(bit, i, c02sr)
        if len(c02sr) == 1:
            break

    oxygen_generator_rating = int(ogr_data[0], 2)
    CO2_scrubber_rating = int(c02sr[0], 2)

    print("Result = " + str(oxygen_generator_rating * CO2_scrubber_rating))
