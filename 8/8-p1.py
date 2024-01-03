
def get_inputs(path):
    file = open(path)
    inst = ''
    out = {}
    for line in file:
        line = line.strip() 
        if '=' not in line and len(line) > 2:
            inst = line
        else:
            bits = line.split(' = ')
            sec = bits[1].split(', ')
            out[bits[0]] = [sec[0][1:], sec[1][:3]]
    return inst, out



inst, dic = get_inputs('input.txt')
count = 0
index = 0
curr = 'AAA'

while curr != 'ZZZ':
    if inst[index] == 'L':
        curr = dic[curr][0]
    else:
        curr = dic[curr][1]
    if len(inst) - 1 > index:
        index += 1
    else:
        index = 0
    count += 1
    print(count, index, curr)

print('DONE')
print(count)