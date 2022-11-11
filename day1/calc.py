


#part1
with open("input.txt") as list:
    lines = [line.strip() for line in list]

new_list = [int(lines[i + 1]) > int(lines[i]) for i in range(len(lines) - 1)]



print(lines)
print(new_list)
print(len(lines))
print(len(new_list))

print(new_list.count(True))

#part2
part2_list = [(int(lines[i + 1]) + int(lines[i+2]) + int(lines[i+3])) > (int(lines[i]) + int(lines[i + 1]) + int(lines[i + 2])) for i in range(len(lines) - 3)]

print(part2_list.count(True))