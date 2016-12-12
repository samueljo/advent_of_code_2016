def has_abba(str):
    for i in range(len(str) - 3):
        if str[i] != str[i + 1] and str[i] == str[i + 3] and str[i + 1] == str[i + 2]:
            return True

    return False

def parse_line(line):
    non_bracket = []
    nb_str = ''

    bracket = []
    b_str = ''

    in_brackets = False

    for i in range(len(line)):
        if in_brackets:
            if line[i] == ']':
                in_brackets = False
                bracket.append(b_str)
                nb_str = ''
            else:
                b_str += line[i]
        else:
            if line[i] == '[':
                in_brackets = True
                non_bracket.append(nb_str)
                b_str = ''
            else:
                nb_str += line[i]

    non_bracket.append(nb_str)
    bracket.append(b_str)

    return [non_bracket, bracket]

def supports_tls(ip):
    non_bracket_abba = False
    bracket_abba = False

    for i in ip[0]:
        if has_abba(i):
            non_bracket_abba = True
            break

    for i in ip[1]:
        if has_abba(i):
            bracket_abba = True
            break

    return non_bracket_abba and not bracket_abba

def count_supported_ips(puzzle_input):
    count = 0
    parsed_ips = []
    for i in puzzle_input:
        parsed_ips.append(parse_line(i))

    for ip in parsed_ips:
        if supports_tls(ip):
            count += 1

    return count

f = open('day_7_input.txt')
puzzle_input = f.readlines()

for i in range(len(puzzle_input)):
    puzzle_input[i] = puzzle_input[i][:-1]

print count_supported_ips(puzzle_input)
