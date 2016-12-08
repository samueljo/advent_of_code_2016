with open('day_1_input.txt') as f:
    steps = f.read().split(', ')

steps[-1] = steps[-1][:-1]

north = 0
facing_north = [True, 1]
# [is facing north or south, is facing north]

east = 0
facing_east = [False, 1]
# [is facing east or west, is facing east]

for stepper in steps:

    if facing_north[0]:
        facing_north[0] = False

        if stepper[0] == 'R':
            east += int(stepper[1:]) * facing_north[1]
            facing_east = [True, 1 * facing_north[1]]
        else:
            east -= int(stepper[1:]) * facing_north[1]
            facing_east = [True, -1 * facing_north[1]]

    else:
        facing_east[0] = False

        if stepper[0] == 'L':
            north += int(stepper[1:]) * facing_east[1]
            facing_north = [True, 1 * facing_east[1]]
        else:
            north -= int(stepper[1:]) * facing_east[1]
            facing_north = [True, -1 * facing_east[1]]

print(abs(north) + abs(east))
