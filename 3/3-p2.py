def make_table(input):
    out = []
    for line in input:
        line = line.rstrip()
        x = []
        for char in line:
            x.append(char)
        out.append(x)
    return out

def is_number(char):
    if 47 < ord(char) < 58:
        return True
    return False

def find_stars(data):
    out = []
    for y, row in enumerate(data):
        for x, col in enumerate(row):
            char = table[y][x]
            if char == '*':
                out.append([y, x]) 
    return out

def find_numbers(data):
    out = []
    for y, row in enumerate(data):
        num = []
        for x, col in enumerate(row):
            char = table[y][x]
            if is_number(char):
                num.append(char)
            else:
                if len(num):
                    out.append(["".join(num), y, x - len(num)])
                    num = []
        if len(num):
            out.append(["".join(num), y, x - len(num)])
    return out

def is_number_nearby(num, y, x):
    for char in range(0, len(num[0])):
        ny = num[1]
        nx = num[2] + char

        if y - 2 < ny < y + 2 and x - 2 < nx < x + 2:
            return True
            
    return False

def calculate(stars, numbers):
    total = 0
    for star in stars:
        res = []
        for num in numbers:
            if is_number_nearby(num, star[0], star[1]):
                res.append(num)
        if len(res) == 2:
            total += int(res[0][0]) * int(res[1][0])
    return total


file = open("3/input.txt")
table = make_table(file)
stars = find_stars(table)
numbers = find_numbers(table)
result = calculate(stars, numbers)

print(result)