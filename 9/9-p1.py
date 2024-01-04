def get_inputs(path):
    file = open(path)
    out = []
    for line in file:
        line = line.strip()
        out.append(list(map(int, line.split(' '))))
    return out

def process(row):
    out = []
    for (index, val) in enumerate(row):
        if index == len(row) - 1:
            break
        out.append(row[index + 1] - row[index])
    return out 

def to_zero_and_add(row):
    out = []
    out.append(row[-1])
    while not all(x == 0 for x in row):
        row = process(row)
        out.append(row[-1])
    out.reverse()
    return out

data = get_inputs('input.txt')
total = 0
for row in data:
    total += sum(to_zero_and_add(row))
print(total)


