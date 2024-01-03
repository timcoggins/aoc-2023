from math import lcm

def get_inputs(path):
    file = open(path)
    inst = ''
    out = {}
    for line in file:
        line = line.strip() 
        if '=' not in line and len(line) > 1:
            inst = line
        else:
            bits = line.split(' = ')
            sec = bits[1].split(', ')
            out[bits[0]] = [sec[0][1:], sec[1][:3]]
    return inst, out

def find_nodes(dic): 
    out = []
    for key in dic.keys():
        if key[-1] == 'A':
            out.append(key)
    return out

def find_factors(inst, dic, nodes):
    factors = []
    for node in nodes:
        curr = node
        x = 0
        count = 0
        while curr[-1] != 'Z':
            if inst[x] == 'L':
                curr = dic[curr][0]
            else:
                curr = dic[curr][1]
            if len(inst) - 1 > x:
                x += 1
            else:
                x = 0
            count += 1
        factors.append(count)
    return factors

inst, dic = get_inputs('input.txt')
nodes = find_nodes(dic)
factors = find_factors(inst, dic, nodes)
res = lcm(*factors)
print(res)