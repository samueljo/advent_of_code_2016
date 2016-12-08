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

def get_triangles_by_column(data):
    triangles = []
    for i in range(0, len(data), 3):
        temp = []
        for j in range(3):
            temp.append(data[i][j])
            temp.append(data[i + 1][j])
            temp.append(data[i + 2][j])
            triangles.append(temp)
            temp = []

    return triangles

with open('day_3_input.txt') as f:
    data = f.readlines()
    for i in range(len(data)):
        data[i] = data[i][:-1].strip().split()
        for j in range(len(data[i])):
            data[i][j] = int(data[i][j])

print count_valid_triangles(data)

vertical_triangles = get_triangles_by_column(data)
print count_valid_triangles(vertical_triangles)
