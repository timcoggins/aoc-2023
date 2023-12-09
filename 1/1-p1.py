data = open("2023/1.txt")

total = 0

for line in data:
    array = []

    for index, char in enumerate(line):
        if 47 < ord(char) < 58:
            array.append(char)

    res = int("".join([array[0], array[-1]]))
    total = total + res

print(total)