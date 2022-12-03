ruck_sack_contents = []
with open('data.txt', 'r') as f:
    for line in f.readlines():
        ruck_sack_contents.append(line.rstrip())

def get_rucksack_compartments(all_contents):
    size = len(all_contents)
    compartment_1 = all_contents[0:int(size/2)]
    compartment_2 = all_contents[int(size/2):]
    return compartment_1, compartment_2

def find_common_letters(comp_1, comp_2):
    common_letters = []
    for letter_1 in comp_1:
        for letter_2 in comp_2:
            if letter_1 == letter_2:
                common_letters.append(letter_2)
    return set(common_letters)

def compute_priority_score(letter_list):
    priority_score = 0
    for letter in letter_list:
        if letter.isupper():
            priority_score += ord(letter) - 38
        if letter.islower():
            priority_score += ord(letter) - 96
    return priority_score

all_common_letters = []
for item in ruck_sack_contents:
    compartment_1, compartment_2 = (get_rucksack_compartments(item))
    all_common_letters.extend(find_common_letters(compartment_1, compartment_2))

# Iterate through the elf groups
letters_to_sum = []
for i in range(int(len(ruck_sack_contents)/3)):
    elf_group = (ruck_sack_contents[i*3:i*3+3])
    first_common_letters = (find_common_letters(elf_group[0], elf_group[1]))
    final_common_letters = (find_common_letters(elf_group[2], first_common_letters))
    letters_to_sum.extend(final_common_letters)

# Solution2
print(compute_priority_score(letters_to_sum))

    
        
# Solution1
print(compute_priority_score(all_common_letters))
