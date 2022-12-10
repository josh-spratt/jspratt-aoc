import sys
print(sys.argv[1])
if sys.argv[1] == 'test':
    data_file = 'test_data.txt'
else:
    data_file   = 'data.txt'

file_system_dict = {}
len_of_last_dir = 1
previous_dir = ''
current_dir = ''
running_ls = False
current_path = ''
current_dir = ''
with open(data_file, 'r') as f:
    for line in f.readlines():
        if line.split()[0] == '$':
            running_ls = False
        if '$ cd' in line:
            if '..' in line:
                split_path = current_path[0:-1].split('/')
                current_dir = split_path[-2]
                current_path = '/'.join(split_path[0:-1])+'/'
            else:
                if line.split()[2] == '/':
                    current_path = '/'
                    file_system_dict[current_path] = {'dirs': [], 'files': [], 'size': 0}
                else:
                    current_dir = line.split()[2]
                    current_path += current_dir+'/'
                    file_system_dict[current_path] = {'dirs': [], 'files': [], 'size': 0}
        if '$ ls' in line:
            running_ls = True
        
        if running_ls:
            if line.split()[0] == 'dir':
                file_system_dict[current_path]['dirs'].append(line.split()[1])
            if line.split()[0].isnumeric():
                file_system_dict[current_path]['files'].append({line.split()[1]: int(line.split()[0])})


        # print(f'{line.rstrip()}---path: {current_path} dir: {current_dir}')
    for key in file_system_dict.keys():
        paths_to_check = [key+dir+'/' for dir in file_system_dict[key]['dirs']]
        dir_sum = 0
        next_layer = []
        for item in paths_to_check:
            if len(file_system_dict[item]['dirs']) !=0:
                next_layer.extend([item+dir+'/' for dir in file_system_dict[item]['dirs']])
        paths_to_check.append(next_layer)
        print(paths_to_check)
        # paths_to_check = {}
        # layer = 0
        # searching = True
        # path_to_search=key
        # while searching:
        #     if len(file_system_dict[key]['dirs']) != 0:
        #         paths_to_check[layer] = []
        #         for dir in paths_to_check[layer]['dirs']:
        #             paths_to_check[layer].append(key+dir+'/')
        #         layer_sum = 0
        #         for item in paths_to_check[layer]:
        #             layer_sum += len(file_system_dict[item]['dirs'])
        #             print(layer_sum)
        #         if layer_sum == 0:
        #             searching = False
        #         layer +=1
            
        #     print(paths_to_check)
            




            

    # for line in f.readlines():
    #     if reading_output:
    #         if '$' in line:
    #             reading_output = False
    #         if 'dir' in line:
    #             file_system_dict[current_dir].append({line.split()[1]: []})
    #         if line.split()[0].isnumeric():
    #             file_system_dict[current_dir].append({'type': 'file', 'name': line.split()[1], 'size': int(line.split()[0])})

    #     if 'ls' in line:
    #         reading_output = True

    #     if 'cd' in line:
    #         current_dir = line.split()[2]
    #         file_system_dict[line.split()[2]] = []



        
        # if 'cd' in line:
        #     command = line.split()[2]
        #     if command == '..':
        #         print('go up a level')
        #         current_dir = previous_dir
        #         print(f'going up a level from directory {previous_dir} to {current_dir}')
        #     else:
        #         previous_dir = current_dir
        #         current_dir = command
        #         print(f'changing current directory to {current_dir} and previous directory to {previous_dir}')
        #     # print(f'changed from directory {previous_dir} to {current_dir}')
            

