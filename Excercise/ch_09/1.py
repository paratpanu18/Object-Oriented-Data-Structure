def is_sorted(numbers_list) -> bool:
    prev = numbers_list[0]
    for number in numbers_list:
        if number < prev:
            return False
        prev = number
    return True

numbers = [int(number) for number in input("Enter Input : ").split()]
print("Yes" if is_sorted(numbers) else "No")