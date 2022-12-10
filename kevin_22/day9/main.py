import sys
print(sys.argv[1])
if sys.argv[1] == 'test':
    data_file = 'test_data.txt'
else:
    data_file   = 'data.txt'

head_location = [0,0]
tail_location = [0,0]
tail_locations = []

long_rope = [[0,0] for i in range(10)]

def city_block_distance(pt1,pt2):
    return abs(pt1[0]-pt2[0]) + abs(pt1[1]-pt2[1])

def compute_new_following_point(pt1, pt2):
    x_diff = pt1[0] - pt2[0]
    y_diff = pt1[1] - pt2[1]
    new_point = pt2
    if city_block_distance(pt1,pt2) == 2:
        if pt1[0] == pt2[0]:
            if pt1[1] > pt2[1]:
                new_point[1] = pt1[1] - 1
            if pt1[1] < pt2[1]:
                new_point[1] = pt1[1] + 1
        if pt1[1] == pt2[1]:
            if pt1[0] > pt2[0]:
                new_point[0] = pt1[0] - 1
            if pt1[0] < pt2[0]:
                new_point[0] = pt1[0] + 1
                    
    if city_block_distance(pt1,pt2) == 3:
        if x_diff == 2 and abs(y_diff) == 1:
                new_point[1] = pt1[1]
                new_point[0] = pt1[0]-1
        if x_diff == -2 and abs(y_diff) == 1:
                new_point[1] = pt1[1]
                new_point[0] = pt1[0]+1
        if abs(x_diff) == 1 and y_diff == 2:
                new_point[0] = pt1[0]
                new_point[1] = pt1[1]-1
        if abs(x_diff) == 1 and y_diff == -2:
                new_point[0] = pt1[0]
                new_point[1] = pt1[1]+1
    
    if city_block_distance(pt1,pt2) > 3:
        if x_diff > 0 and y_diff > 0:
                new_point[0] = pt1[1]-1
                new_point[1] = pt1[1]-1
        if x_diff < 0 and y_diff > 0:
                new_point[0] = pt1[1]+1
                new_point[1] = pt1[1]-1
        if x_diff > 0 and y_diff < 0:
                new_point[0] = pt1[1]-1
                new_point[1] = pt1[1]+1
        if x_diff < 0 and y_diff < 0:
                new_point[0] = pt1[1]+1
                new_point[1] = pt1[1]+1
    return new_point

with open(data_file, 'r') as f:
    for line in f.readlines():
        direction, number = line.split()[0], int(line.split()[1])
        for i in range(number):
            # update head location
            if direction == 'R':
                long_rope[0][0] += 1
            if direction == 'L':
                long_rope[0][0] -= 1
            if direction == 'U':
                long_rope[0][1] += 1
            if direction == 'D':
                long_rope[0][1] -= 1
        # compute the rest of the rope
            for i in range(len(long_rope)-1):
                new_point = compute_new_following_point(long_rope[i], long_rope[i+1])
                long_rope[i+1] = new_point
                # print(f"Comparing {long_rope[i]} and {long_rope[i+1]} new tail location is {compute_new_following_point(long_rope[i], long_rope[i+1])}")
            tail_locations.append(list(long_rope[-1]))
    
    print(list(set(tuple(p) for p in tail_locations)))
    print(len(list(set(tuple(p) for p in tail_locations))))


                

            




