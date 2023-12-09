def make():
    file = open("3/input.txt")
    out = []
    for line in file:
        line = line.rstrip()
        x = []
        for char in line:
            x.append(char)
        out.append(x)
    return out

def is_symbol(char):
    if char != '.' and (ord(char) > 58 or ord(char) < 48):
        return True
    return False

def in_range(x, y):
    if 0 <= x <= 139 and 0 <= y <= 139:
        return True
    return False

def check(y, x, len):
    for l in range(y - 1, y + 2): # rows
        for index in range(x - 1, x + len + 1):
            if in_range(index, l):
                current = table[l][index]
                if is_symbol(current):
                    return True
    return False


table = make()
y = 0
total = 0

while y < len(table):
    x = 0
    numbers = []

    while x < len(table[0]):

        if 47 < ord(table[y][x]) < 58:
            z = 0
            num = []
            cur = table[y][x]

            while 47 < ord(cur) < 58: 
                num.append(cur)
                z += 1

                if in_range(y, x + z):
                    cur = table[y][x + z]
                else:
                    break

            if check(y, x, len(num)):
                numbers.append("".join(num))

            x += z
        x += 1

    print(y, 'valid', numbers)

    for n in numbers:
        total += int(n)
    y += 1

print(total)
