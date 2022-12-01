with open('data.txt', 'r') as f:
    data = []
    temp = 0
    elf_calorie_list = []
    for line in f.readlines():
        if line.rstrip() != '':
            temp += (int(line.rstrip()))
        else:
            elf_calorie_list.append(temp)
            temp = 0

sorted_data = (sorted(elf_calorie_list))
print(sorted_data[-1])
print(sorted_data[-1]+sorted_data[-2]+sorted_data[-3])