def find_total_distance(steps):
    pos = [0, 0]
    facing_north = [True, 1]
    # [is facing north or south, is facing north]
    facing_east = [False, 1]
    # [is facing east or west, is facing east]

    for step in steps:
        if facing_north[0]:
            facing_north[0] = False
            pos, facing_north, facing_east = east_west_step(pos, step, facing_north, facing_east)
        else:
            facing_east[0] = False
            pos, facing_north, facing_east = north_south_step(pos, step, facing_north, facing_east)

    return abs(pos[0]) + abs(pos[1])

def find_first_repeated_pos(steps):
    visited = { '0 0': True }
    pos = [0, 0]
    facing_north = [True, 1]
    facing_east = [False, 1]

    for step in steps:
        prev_pos = pos[:]

        if facing_north[0]:
            facing_north[0] = False
            pos, facing_north, facing_east = east_west_step(pos, step, facing_north, facing_east)

        else:
            facing_east[0] = False
            pos, facing_north, facing_east = north_south_step(pos, step, facing_north, facing_east)

        visited, target_pos = travel_to_pos(visited, prev_pos, pos)

        if target_pos:
            return abs(target_pos[0]) + abs(target_pos[1])

    return None

def travel_to_pos(visited, prev_pos, pos):
    temp_pos = prev_pos[:]

    if prev_pos[0] == pos[0]:
        path_idx = 1
    else:
        path_idx = 0

    if prev_pos[path_idx] < pos[path_idx]:
        while temp_pos[path_idx] < pos[path_idx]:
            temp_pos[path_idx] += 1
            temp = "{0} {1}".format(temp_pos[0], temp_pos[1])
            if temp in visited:
                return [visited, temp_pos]
            else:
                visited[temp] = True
    else:
        while temp_pos[path_idx] > pos[path_idx]:
            temp_pos[path_idx] -= 1
            temp = "{0} {1}".format(temp_pos[0], temp_pos[1])
            if temp in visited:
                return [visited, temp_pos]
            else:
                visited[temp] = True

    return [visited, None]

def north_south_step(pos, step, facing_north, facing_east):
    if step[0] == 'L':
        pos[0] += int(step[1:]) * facing_east[1]
        facing_north = [True, 1 * facing_east[1]]
    else:
        pos[0] -= int(step[1:]) * facing_east[1]
        facing_north = [True, -1 * facing_east[1]]
    return [pos, facing_north, facing_east]

def east_west_step(pos, step, facing_north, facing_east):
    if step[0] == 'R':
        pos[1] += int(step[1:]) * facing_north[1]
        facing_east = [True, 1 * facing_north[1]]
    else:
        pos[1] -= int(step[1:]) * facing_north[1]
        facing_east = [True, -1 * facing_north[1]]
    return [pos, facing_north, facing_east]

with open('day_1_input.txt') as f:
    steps = f.read().split(', ')
    steps[-1] = steps[-1][:-1]

print(find_total_distance(steps))
print(find_first_repeated_pos(steps))
