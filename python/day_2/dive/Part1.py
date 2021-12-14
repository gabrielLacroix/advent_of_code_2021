if __name__ == '__main__':

    total_depth = 0
    total_position = 0

    def forward(horizontal_shift):
        global total_position
        total_position += horizontal_shift

    def dive(depth):
        global total_depth
        total_depth += depth

    funcs = {'forward': lambda i: forward(i),
             'up': lambda i: dive(-i),
             'down': lambda i: dive(i)}

    def get_action(action):
        for i, (action_name, func) in enumerate(funcs):
            if action_name == action:
                return funcs[i]

    data = open('input').read().split('\n')
    for line in data:
        action_amount = line.split(' ')
        if len(action_amount) == 2:
            action, x = action_amount
            funcs.get(action)(int(x))

    print("Depth = " + str(total_depth))
    print("Position = " + str(total_position))
    print("Result = " + str(total_depth * total_position))
