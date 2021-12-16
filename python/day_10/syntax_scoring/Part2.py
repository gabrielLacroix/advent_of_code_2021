if __name__ == '__main__':
    data = open('input').read().split('\n')
    data.remove('')

    openers = ['(', '[', '{', '<']

    completion_character_scores = {')': 1, ']': 2, '}': 3, '>': 4, '': 0}
    opener_to_closer = {'(': ')', '[': ']', '{': '}', '<': '>'}

    def find_completion_character(source):
        completion_characters = []
        if find_first_illegal_character(source) != '':
            return completion_characters
        for c in source:
            if c in openers:
                completion_characters.append(opener_to_closer.get(c))
            else:
                completion_characters.pop()
        completion_characters.reverse()
        return completion_characters

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

    def compute_score(completion_string):
        result = 0
        for c in completion_string:
            result *= 5
            result += completion_character_scores.get(c)
        return result

    scores = []
    for line in data:
        completion_character = find_completion_character(line)
        score = compute_score(completion_character)
        if score != 0:
            scores.append(score)
    scores.sort()
    print(scores[len(scores)//2])
