with open('data.txt', 'r') as f:
    # Pt1
    overlapping_pairs = 0
    overlapping_pairs_2 = 0

    for line in f.readlines():
        elf_1, elf_2 = (line.rstrip().split(','))
        elf_1 = [int(x) for x in elf_1.split('-')]
        elf_2 = [int(x) for x in elf_2.split('-')]
        print(line)
        # Is elf_1 assignment contained in elf_2
        if elf_1[0] >= elf_2[0] and elf_1[1] <= elf_2[1]:
            print('elf1 assignment contained in elf2 assignment')
            overlapping_pairs += 1

        # Is elf_2 assignment contained in elf_1
        elif elf_2[0] >= elf_1[0] and elf_2[1] <= elf_1[1]:
            print('elf2 assignment contained in elf1 assignment')
            overlapping_pairs += 1

        if elf_1[0] >= elf_2[0] and elf_1[0] <= elf_2[1]:
            print('elf1 assignment contained in elf2 assignment')
            overlapping_pairs_2 += 1

        # Is elf_2 assignment contained in elf_1
        elif elf_2[0] >= elf_1[0] and elf_2[0] <= elf_1[1]:
            print('elf2 assignment contained in elf1 assignment')
            overlapping_pairs_2 += 1

    print(overlapping_pairs_2)
