import sys
print(sys.argv[1])
if sys.argv[1] == 'test':
    data_file = 'test_data.txt'
else:
    data_file   = 'data.txt'

def all_character_are_unique(s):
    if len(set(s)) == 14:
        return True
    else:
        return False

test_dict = {}
with open(data_file, 'r') as f:
    solution_string = ''
    counter = 0
    code_counter = 0
    for line in f.readlines():
        input_buffer = (line.rstrip())    
        for i in range(len(input_buffer)):
            print(input_buffer[i:i+14])
            if all_character_are_unique(input_buffer[i:i+14]):
                print(i+14)
                break
            
            

