def count_valid_triangles(triangles):
    count = 0
    for triangle in triangles:
        if is_valid_triangle(triangle):
            count += 1

    return count

def is_valid_triangle(dimensions):
    other_sum = get_other_sum(dimensions)
    for i in range(len(dimensions)):
        if other_sum[i] <= dimensions[i]:
            return False
    return True

def get_other_sum(dimensions):
    other_sum = [0, 0, 0]
    temp_sum = 0

    for i in range(len(dimensions)):
        other_sum[i] += temp_sum
        temp_sum += dimensions[i]
    temp_sum = 0

    for j in range(len(dimensions) - 1, -1, -1):
        other_sum[j] += temp_sum
        temp_sum += dimensions[j]

    return other_sum

with open('day_3_input.txt') as f:
    triangles = f.readlines()
    for i in range(len(triangles)):
        triangles[i] = triangles[i][:-1].strip().split()
        for j in range(len(triangles[i])):
            triangles[i][j] = int(triangles[i][j])

print count_valid_triangles(triangles)
