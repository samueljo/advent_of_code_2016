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
                result += repeat_str * multiplier
                repeat_str = ''
                sequence = ''
            else:
                count -= 1
        elif marker:
            if i == ')':
                sequence = sequence.split('x')
                count = int(sequence[0])
                multiplier = int(sequence[1])
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

def decompress2(content):
    result = [1] * len(content)
    length = 0
    marker = False
    sequence = ''

    for i in range(len(result)):
        if marker:
            if content[i] == ')':
                sequence = sequence.split('x')
                count = int(sequence[0])
                multiplier = int(sequence[1])
                for j in range(i + 1, i + count + 1):
                    result[j] *= multiplier
                marker = False
                sequence = ''
            else:
                sequence += content[i]
        else:
            if content[i] == '(':
                marker = True
            else:
                length += result[i]

    return length

f = open('day_9_input.txt')
content = f.readlines()[0][:-1]

# print(decompress2('ADVENT'))
# print(decompress2('(3x3)XYZ'))
# print(decompress2('X(8x2)(3x3)ABCY'))
# print(decompress2('(27x12)(20x12)(13x14)(7x10)(1x12)A'))
# print(decompress2('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN'))
# print len(decompress(content))
print decompress2(content)
