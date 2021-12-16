if __name__ == '__main__':
    data = open('input').read().split('\n')
    data.remove('')

    openers = ['(', '[', '{', '<']

    illegal_character_scores = {')': 3, ']': 57, '}': 1197, '>': 25137, '': 0}
    opener_to_closer = {'(': ')', '[': ']', '{': '}', '<': '>'}

    def find_first_illegal_character(source):
        expected_closer = []
        for c in source:
            if c in openers:
                expected_closer.append(opener_to_closer.get(c))
            else:
                closer = expected_closer.pop()
                if c != closer:
                    return c
        return ''

    score = 0
    for line in data:
        first_illegal_character = find_first_illegal_character(line)
        score += illegal_character_scores.get(first_illegal_character)
    print(score)
