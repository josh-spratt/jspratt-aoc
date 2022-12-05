test_stacks = [['Z','N'],['M','C','D'],['P']]
real_stack = [['P','F','M','Q','W','G','R','T'],['H','F','R'],['P','Z','R','V','G','H','S','D'],['Q','H','P','B','F','W','G'],['P','S','M','J','H'],['M','Z','T','H','S','R','P','L'],['P','T','H','N','M','L'],['F','D','Q','R'], ['D','S','C','N','L','P','H']]

move_list = []
with open('data.txt', 'r') as f:
    for line in f.readlines():
        data = line.rstrip()
        print(data.split())
        move_list.append([data.split()[1],data.split()[3],data.split()[5]])

# print(move_list)
# for order in move_list:
#     number_to_move = int(order[0])
#     stack_to_take_from = int(order[1])
#     stack_to_give_to = int(order[2])
#     for i in range(number_to_move):
#         crane_is_holding = real_stack[stack_to_take_from-1].pop()
#         real_stack[stack_to_give_to-1].append(crane_is_holding)

for order in move_list:
    number_to_move = int(order[0])
    stack_to_take_from = int(order[1])
    stack_to_give_to = int(order[2])
    crane_is_holding = test_stacks[stack_to_take_from-1][-1*number_to_move:]
    test_stacks[stack_to_give_to-1].extend(crane_is_holding)
    for i in range(number_to_move):
        crane_is_holding = test_stacks[stack_to_take_from-1].pop()

for item in test_stacks:
    print(item[-1])
