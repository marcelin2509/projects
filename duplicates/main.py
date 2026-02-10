def remove_duplicates(lst: list[int]) -> int:

# makes a set with only unique values while iterating through the list 
# if a value is already in the set, it is replaced with None.
    values = set()
    for i in range(len(lst)):
        if lst[i] in values:
            lst[i] = None
        else:
            values.add(lst[i])

# removes all None values from the list and returns the length of the list
#  which is now the number of unique values.
    lst[:] = [x for x in lst if x is not None]
    return len(lst)

# prompts the user to input a list of integers, 
# calls the remove_duplicates function, 
# and prints the number of unique integers and the list of unique integers.
print("type a list of integers separated by spaces:")
input_list = list(map(int, input().split()))
print("the number of unique integers in the list is:")
print(remove_duplicates(input_list))
print("the list of unique integers is:")
print(input_list)