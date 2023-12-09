def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)

def get_second(n):  
    return n[1]  

data = open("2023/1.txt")

total = 0
words = [("zero", "0"), ("one", "1"), ("two", "2"), ("three", "3"), ("four", "4"), ("five", "5"), ("six", "6"), ("seven", "7"), ("eight", "8"), ("nine", "9") ]

for line in data:
    array = []

    for index, char in enumerate(line):
        if 47 < ord(char) < 58:
            tup = (char, index)
            array.append(tup)

    for number, replacement in words:
        loc_list = find_all(line, number) 

        for location in loc_list:
            if location != -1:
                tup = (replacement, location)
                array.append(tup)

    sort = sorted(array, key=get_second)
    res = int("".join([sort[0][0], sort[-1][0]]))
    total = total + res

print(total)