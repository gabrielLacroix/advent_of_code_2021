if __name__ == '__main__':

    total_depth = 0
    total_position = 0
    aim = 0

    def forward(horizontal_shift):
        global total_position, total_depth, aim
        total_position += horizontal_shift
        dive(aim * horizontal_shift)

    def dive(depth):
        global total_depth
        total_depth += depth

    def aim_up(shift):
        global aim
        aim -= shift

    def aim_down(shift):
        global aim
        aim += shift

    funcs = [('forward', lambda i: forward(i)),
             ('up', lambda i: aim_up(i)),
             ('down', lambda i: aim_down(i))]

    def get_func(action):
        return get_action(action)[1]

    def get_action(action):
        for i, (action_name, func) in enumerate(funcs):
            if action_name == action:
                return funcs[i]

    data = open('input').read().split('\n')
    for line in data:
        action_amount = line.split(' ')
        if len(action_amount) == 2:
            action, x = action_amount
            get_func(action)(int(x))

    print("Depth = " + str(total_depth))
    print("Position = " + str(total_position))
    print("Result = " + str(total_depth * total_position))
