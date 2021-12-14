if __name__ == '__main__':
    data = open('input').read().split('\n')

    number_of_bits = len(data[0])
    data.remove('')
    result_bits = []

    def get_bits(bit_array):
        return [int(bit) for bit in bit_array]

    for i in range(number_of_bits):
        result_bits.append(0)

    for bit_array in data:
        bits = get_bits(bit_array)
        for i in range(number_of_bits):
            result_bits[i] += bits[i]

    most_common = []
    for result in result_bits:
        most_common.append(1 if result > len(data)//2 else 0)
    less_common = [x ^ 1 for x in most_common]

    most_common = ''.join([str(bit) for bit in most_common])
    less_common = ''.join([str(bit) for bit in less_common])

    most_common = int(most_common, 2)
    less_common = int(less_common, 2)

    print("Result = " + str(most_common * less_common))
