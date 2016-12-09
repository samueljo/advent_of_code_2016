def sum_sector_ids(rooms):
    real_rooms = get_real_rooms(rooms)
    total_sum = 0
    for room in real_rooms:
        sector_id = int(room.split('-')[-1].split('[')[0])
        total_sum += sector_id

    return total_sum

def get_real_rooms(rooms):
    real_rooms = []
    for room in rooms:
        if is_real_room(room):
            real_rooms.append(room)

    return real_rooms

def is_real_room(room):
    name = room.split('-')[:-1]
    letter_map = get_letter_map(name)
    sorted_letters = sort_by_freq(letter_map.items())

    return matching_checksums(sorted_letters, room.split('[')[1])

def matching_checksums(sorted_letters, given):
    checksum = ''
    for i in range(5):
        checksum += sorted_letters[i][0]

    return checksum == given[:-1]

def sort_by_freq(items):
    if len(items) <= 1:
        return items
    pivot = items[0]
    left = []
    right = []
    for el in items[1:]:
        if el[1] < pivot[1]:
            right.append(el)
        elif el[1] == pivot[1]:
            if el[0] < pivot[0]:
                left.append(el)
            else:
                right.append(el)
        else:
            left.append(el)

    sorted_list = sort_by_freq(left)
    sorted_list.extend([pivot])
    sorted_list.extend(sort_by_freq(right))
    return sorted_list

def get_letter_map(name):
    letter_map = {}
    for el in name:
        for i in range(len(el)):
            if el[i] in letter_map:
                letter_map[el[i]] += 1
            else:
                letter_map[el[i]] = 1

    return letter_map


f = open('day_4_input.txt')
rooms = f.readlines()

for i in range(len(rooms)):
    rooms[i] = rooms[i][:-1]

print sum_sector_ids(rooms)
