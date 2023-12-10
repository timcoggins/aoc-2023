def clean(parts):
    out = []
    for num in parts.lstrip().rstrip().split(" "):
        if (num != " " and num != ''):
            out.append(int(num))
    return out


def get_inputs(path):
    file = open(path)
    out = []

    for line in file:
        parts = line.strip().split(":")[1].split('|')
        wins = clean(parts[0])
        mine = clean(parts[1])
        out.append([wins, mine])
    return out

def process(game):
    points = 0
    for win in game[0]:
        if win in game[1]:
            if points == 0:
                points += 1
            else: 
                points *= 2
    return points


games = get_inputs('4/input.txt')
total = 0
for index, game in enumerate(games):
    total += process(game) 
print(total)
    


