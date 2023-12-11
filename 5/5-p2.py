
def get_input():
    file = open('5/input.txt')
    chunks = file.read().split('\n')
    while("" in chunks):
        chunks.remove("")
    next = chunks[0].split(': ')[1].rstrip().split(" ")
    seeds = [int(i) for i in next]
    x = 1
    maps = []
    current = []
    while x < len(chunks):
        if 'map:' in chunks[x]:
            if len(current):
                maps.append(current)
            current = []
        else:
            current.append(chunks[x])
        x += 1
    if len(current):
        maps.append(current)
    return seeds, maps


def soil_map(val, dest, source, length):
    if source <= val < source + length:
        return (dest - source) + val
    else:
        return val

def in_ranges(val, ranges):
    values = []
    for current in ranges:
        bits = current.split(" ")
        splits = [int(i) for i in bits]
        new = soil_map(val, splits[0], splits[1], splits[2])
        if new != val:
            values.append(new)
    if len(values) > 0:
        return values[0]
    else:
        return val
    
    
seeds, maps = get_input()
res = []

x = 0
pairs = []
while x < len(seeds):
    pairs.append([seeds[x], seeds[x+1]])
    x += 2

print(pairs)

# quit()
# pairs = [[79, 14], [55, 13]]

for pair in pairs:
    for seed in range(pair[0], pair[0] + pair[1]):
        x = seed
        for bit in maps:
            x = in_ranges(x, bit)
        res.append(x)
        print(x)

print(res)
print('the end is')
print(sorted(res)[0])

# 111627841