def main():
    # Read input file
    with open("josh_22/input_files/day1.txt") as f:
        list_of_cals = [x.rstrip() for x in f.readlines()]
    
    # Break list into separate lists based on empty string separator
    list_chunks = []
    x = 0
    list_chunks.append([])
    for i in list_of_cals:
        if i != '':
            list_chunks[x].append(i)
        else:
            x += 1
            list_chunks.append([])
    
    # Create a new list that contains the sum for each list
    new_list = []
    for list_chunk in list_chunks:
        new_list.append(sum([int(i) for i in list_chunk]))
    
    # Get the max value from the list
    print(sorted(new_list))
        

if __name__ == "__main__":
    main()
