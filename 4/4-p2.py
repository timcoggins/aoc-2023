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

def process(games, start=0, depth=0):
    if len(games) <= start:
        return 0
    print(depth * '=')

    count = 0
    res = 1
    for win in games[start][0]:
        if win in games[start][1]:
            count += 1
    for i in range(start + 1, start + count + 1):
        res += process(games, i, depth + 1)
    return res


games = get_inputs('4/input.txt')

total = 0
for index, val in enumerate(games):
    total += process(games, index, 1)

print('TOTAL', total)
    


