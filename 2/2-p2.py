file = open("2/input.txt")
total = 0

for line in file:
    line = line.rstrip()
    rounds = line.split(":")[1].split(";")
    green = 0
    red = 0
    blue = 0

    for round in rounds:
        x = round.split(",")

        for cube in x:
            y = cube.lstrip().split(" ")
            if y[1] == 'red' and red < int(y[0]):
                red = int(y[0])
            if y[1] == 'green' and green < int(y[0]):
                green = int(y[0])
            if y[1] == 'blue' and blue < int(y[0]):
                blue = int(y[0])

    total += (green * blue * red)

print(total)