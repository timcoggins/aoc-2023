file = open("2/input.txt")
total = 0

for line in file:
    line = line.rstrip()
    game = int(line.split(":")[0].split(" ")[1])
    rounds = line.split(":")[1].split(";")
    valid = True

    for round in rounds:
        green = 0
        red = 0
        blue = 0
        x = round.split(",")

        for cube in x:
            y = cube.lstrip().split(" ")
            if y[1] == 'red':
                red += int(y[0])
            if y[1] == 'green':
                green += int(y[0])
            if y[1] == 'blue':
                blue += int(y[0])
            if red > 12 or green > 13 or blue > 14:
                valid = False

    if valid == True:
        total += game
    
print(total)