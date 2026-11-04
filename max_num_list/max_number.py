def find_max_number(numbers):
    if not numbers:
        return None
    max_number = numbers[0]
    for num in numbers:
        if num>max_number:
            max_number = num
    return max_number

max_num = find_max_number([3, 5, 2, 8, 1])
print("The maximum number is:", max_num)