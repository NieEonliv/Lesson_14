def print_array(list):
    if len(list) == 0:
        print("Empty list")
        return

    print(list.pop(0))
    print_array(list)

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

print_array(my_list.copy())