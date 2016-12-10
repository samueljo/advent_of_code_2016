def repetition_code(corrupt_code):
    code = ''
    repetition_count = {}

    for i in range(len(corrupt_code[0])):
        repetition_count[i] = {}

    for row in corrupt_code:
        for i in range(len(row)):
            current_el = row[i]
            if current_el in repetition_count[i]:
                repetition_count[i][current_el] += 1
            else:
                repetition_count[i][current_el] = 1

    for i in repetition_count.keys():
        temp = sorted(repetition_count[i].items(), key=lambda x: x[1])[0]
        code += temp[0]

    return code

f = open('day_6_input.txt')
puzzle_input = f.readlines()

for i in range(len(puzzle_input)):
    puzzle_input[i] = puzzle_input[i][:-1]

print repetition_code(puzzle_input)
