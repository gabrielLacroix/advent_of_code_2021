if __name__ == '__main__':
    data = open('input').read().split('\n')

    draw_numbers = data.pop(0).split(',')
    data.remove('')

    def check_horizontal(values):
        bingo = False
        for value_line in values:
            bingo = bingo or all(value_line)
        return bingo

    def check_vertical(values):
        return check_horizontal(list(zip(*values[::-1])))

    class Board:
        def __init__(self, values):
            self.values = values
            self.verif = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
            self.won = False

        def check_value(self, new_value):
            for x, value_line in enumerate(self.values):
                for y, value in enumerate(value_line):
                    if new_value == value:
                        self.verif[x][y] = 1
                        self.check_has_bingo()
                        return

        def check_has_bingo(self):
            bingo = False
            bingo = bingo or check_horizontal(self.verif)
            bingo = bingo or check_vertical(self.verif)
            self.won = bingo


    boards = []
    next_board_values = []
    for numbers in data:
        if numbers == '':
            boards.append(Board(next_board_values))
            next_board_values = []
        else:
            next_board_values.append(numbers.split())

    done = False
    last_call = 0
    unmarked = 0
    for number in draw_numbers:
        if done:
            break
        for board in boards:
            board.check_value(number)
            if board.won:
                done = True
                last_call = int(number)

                for x, line in enumerate(board.verif):
                    for y, val in enumerate(line):
                        board_number = board.values[x][y]
                        if val == 0:
                            unmarked += int(board_number)

    print("Result = " + str(unmarked * last_call))
