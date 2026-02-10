def merge_two_lists(list1: list, list2: list) -> list:

    for num in list1:
        list2.append(num)
        
    list2.sort()
    return list2

print("please enter the first list of numbers, separated by spaces:")
list1 = list(map(int, input().split()))

print("please enter the second list of numbers, separated by spaces:")
list2 = list(map(int, input().split()))

merged_list = merge_two_lists(list1, list2)
print("the merged list is:", merged_list)