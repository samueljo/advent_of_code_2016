def decompress(content):
    result = ''
    marker = False
    repeat = False
    sequence = ''
    repeat_str = ''
    count = 0

    for i in content:
        if repeat:
            repeat_str += i
            if count == 1:
                repeat = False
                result += repeat_str * multipler
                repeat_str = ''
                sequence = ''
            else:
                count -= 1
        elif marker:
            if i == ')':
                sequence = sequence.split('x')
                count = int(sequence[0])
                multipler = int(sequence[1])
                marker = False
                repeat = True
            else:
                sequence += i
        else:
            if i == '(':
                marker = True
            else:
                result += i

    return result

f = open('day_9_input.txt')
content = f.readlines()[0][:-1]

# print(len(decompress('ADVENT')))
# print(len(decompress('A(1x5)BC')))
# print(len(decompress('(3x3)XYZ')))
# print(len(decompress('A(2x2)BCD(2x2)EFG')))
# print(len(decompress('(6x1)(1x3)A')))
# print(len(decompress('X(8x2)(3x3)ABCY')))
print len(decompress(content))
