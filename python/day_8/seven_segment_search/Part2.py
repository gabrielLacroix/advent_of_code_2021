if __name__ == '__main__':
    data = open('input').read().split('\n')
    data.remove('')

    def find_value_of_len(source, n):
        for value in source:
            if len(value) == n:
                return value

    def remove_char(source, to_remove):
        result = source
        for char in to_remove:
            result = result.replace(char, '')
        return result

    def find_segment_9(four, seven, len_6_values):
        for value in len_6_values:
            stripped = remove_char(value, four)
            stripped = remove_char(stripped, seven)
            if len(stripped) == 1:
                return value, stripped

    def find_segment_G(eight, nine):
        return remove_char(eight, nine)

    def find_segment_6(one, len_6_values):
        for value in len_6_values:
            if len(remove_char(value, one)) == 5:
                return value

    def find_segment_0(six, nine, len_6_values):
        len_6_values.remove(six)
        len_6_values.remove(nine)
        return len_6_values[0]


    valid_digits = [2, 3, 4, 7]
    count = 0
    for entry in data:
        pipe = entry.index('|')

        unique_signal_patterns, output = entry.split('|')
        unique_signal_patterns = unique_signal_patterns.split(' ')
        unique_signal_patterns.remove('')

        segment_1 = find_value_of_len(unique_signal_patterns, 2)
        segment_7 = find_value_of_len(unique_signal_patterns, 3)
        segment_4 = find_value_of_len(unique_signal_patterns, 4)
        segment_8 = find_value_of_len(unique_signal_patterns, 7)

        segment_D_value = remove_char(segment_7, segment_1)
        segment_E_and_F_values = remove_char(segment_4, segment_1)

        signals_of_6_segment = [x for x in unique_signal_patterns if len(x) == 6]
        segment_9, segment_C_value = find_segment_9(segment_4, segment_7, signals_of_6_segment)

        segment_G_value = find_segment_G(segment_8, segment_9)
        segment_6 = find_segment_6(segment_1, signals_of_6_segment)
        segment_0 = find_segment_0(segment_6, segment_9, signals_of_6_segment)

        segment_F_value = remove_char(segment_8, segment_0)
        segment_E_value = remove_char(segment_E_and_F_values, segment_F_value)
        segment_A_value = remove_char(segment_1, segment_6)
        segment_B_value = remove_char(segment_1, segment_A_value)

        def find_number(segments):
            if len(segments) == 2:
                return 1
            if len(segments) == 3:
                return 7
            if len(segments) == 4:
                return 4
            if len(segments) == 7:
                return 8
            if len(segments) == 6:
                if segment_F_value not in segments:
                    return 0
                if segment_A_value not in segments:
                    return 6
                return 9
            if len(segments) == 5:
                if segment_B_value not in segments:
                    return 2
                if segment_A_value not in segments:
                    return 5
                return 3
        output = output.split(' ')
        output.remove('')
        res_str = ''
        for number in output:
            res_str += str(find_number(number))

        count += int(res_str)
    print(count)