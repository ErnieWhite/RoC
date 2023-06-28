def rotate(t):
    temp = t.pop(0)
    t.append(temp)
    return t

with open('input.txt', 'r', encoding='utf-8') as data:
    lines = data.readlines()

triangle = [0,0,0]
count = 0

for line in lines:
    triangle[0] = int(line[:5].strip())
    triangle[1] = int(line[5:10].strip())
    triangle[2] = int(line[10:15].strip())
    is_triangle = True
    for i in range(3):
        if triangle[0] + triangle[1] <= triangle[2]:
            is_triangle = False
            break
        triangle = rotate(triangle)

    if is_triangle:
        count += 1


print(count)

