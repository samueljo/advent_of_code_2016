def rotate(l, n):
    return l[-n:] + l[:-n]

def rotate_row(screen, instruction):
    instruction = instruction.split()
    row = int(instruction[2].split('=')[1])
    shift = int(instruction[-1])

    screen[row] = rotate(screen[row], shift)
    return screen

def rotate_col(screen, instruction):
    screen = [list(x) for x in zip(*screen)]
    screen = rotate_row(screen, instruction)
    screen = [list(x) for x in zip(*screen)]
    return screen

def rect(screen, instruction):
    dim = instruction.split()[1].split('x')
    for row in range(int(dim[1])):
        for col in range(int(dim[0])):
            screen[row][col] = 1
    return screen

def read_instruction(screen, instruction):
    if 'rotate row' in instruction:
        screen = rotate_row(screen, instruction)
    elif 'rotate column' in instruction:
        screen = rotate_col(screen, instruction)
    elif 'rect' in instruction:
        screen = rect(screen, instruction)

    return screen

def fill_screen(instructions):
    screen = [[0 for x in range(50)] for y in range(6)]

    for instruction in instructions:
        screen = read_instruction(screen, instruction)

    return screen

def count_lit_pixels(screen):
    count = 0

    for row in screen:
        count += sum(row)

    return count

f = open('day_8_input.txt')
instructions = f.readlines()

for i in range(len(instructions)):
    instructions[i] = instructions[i][:-1]

screen = fill_screen(instructions)
print count_lit_pixels(screen)
