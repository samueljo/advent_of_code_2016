# in_bounds function for part I
# def in_bounds(pos):
#     return pos[0] <= 2 and pos[0] >= 0 and pos[1] <= 2 and pos[1] >= 0

# pos_to_buttons function for part I
# def pos_to_buttons(positions):
#     code = ''
#     for pos in positions:
#         if pos == [0, 0]:
#             button = '1'
#         elif pos == [0, 1]:
#             button = '2'
#         elif pos == [0, 2]:
#             button = '3'
#         elif pos == [1, 0]:
#             button = '4'
#         elif pos == [1, 1]:
#             button = '5'
#         elif pos == [1, 2]:
#             button = '6'
#         elif pos == [2, 0]:
#             button = '7'
#         elif pos == [2, 1]:
#             button = '8'
#         elif pos == [2, 2]:
#             button = '9'
#
#         code += button
#
#     return code

# in_bounds function for part II
def in_bounds(pos):
    if (pos[0] == 0 or pos[0] == 4) and pos[1] == 2:
        return True
    elif (pos[0] == 1 or pos[0] == 3) and 1 <= pos[1] <= 3:
        return True
    elif pos[0] == 2 and 0 <= pos[1] <= 4:
        return True
    else:
        return False

# pos_to_buttons functions for part II
def pos_to_buttons(positions):
    code = ''
    for pos in positions:
        if pos == [0, 2]:
            button = '1'
        elif pos == [1, 1]:
            button = '2'
        elif pos == [1, 2]:
            button = '3'
        elif pos == [1, 3]:
            button = '4'
        elif pos == [2, 0]:
            button = '5'
        elif pos == [2, 1]:
            button = '6'
        elif pos == [2, 2]:
            button = '7'
        elif pos == [2, 3]:
            button = '8'
        elif pos == [2, 4]:
            button = '9'
        elif pos == [3, 1]:
            button = 'A'
        elif pos == [3, 2]:
            button = 'B'
        elif pos == [3, 3]:
            button = 'C'
        elif pos == [4, 2]:
            button = 'D'

        code += button

    return code


def find_next_pos(pos, direction):
    for i in range(len(direction)):
        if direction[i] == 'U':
            if in_bounds([pos[0] - 1, pos[1]]):
                pos = [pos[0] - 1, pos[1]]
        elif direction[i] == 'D':
            if in_bounds([pos[0] + 1, pos[1]]):
                pos = [pos[0] + 1, pos[1]]
        elif direction[i] == 'L':
            if in_bounds([pos[0], pos[1] - 1]):
                pos = [pos[0], pos[1] - 1]
        elif direction[i] == 'R':
            if in_bounds([pos[0], pos[1] + 1]):
                pos = [pos[0], pos[1] + 1]

    return pos

def get_code(dirs):
    current_pos = [2, 0]
    code_pos = []

    for direction in dirs:
        current_pos = find_next_pos(current_pos, direction)
        code_pos.append(current_pos)

    return pos_to_buttons(code_pos)

with open('day_2_input.txt') as f:
    dirs = f.readlines()
    for i in range(len(dirs)):
        dirs[i] = dirs[i][:-1]

print get_code(dirs)
