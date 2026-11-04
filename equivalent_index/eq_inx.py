#Given a list of integers, find the index at which the sum of the left half of the list is equal to the right half.

# If there is no index where this condition is satisfied return -1.

integer = [1, 7, 3, 6, 5]





def find_equivalent(lst):
    for i, num in enumerate(lst):
        left_sum = sum(lst[:i + 1])
        if left_sum == sum(lst[i + 1:]):
            return i
    return -1

# print(find_equivalent(integer))


#the other way
def find_eq(lst):
    for i in range(len(lst)):
        if sum(lst[:i+1]) == sum(lst[i + 1:]):
            return i
    return -1
print(find_eq(integer))
