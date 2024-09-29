def sort_by_freqency(numbers):
    numbers_dict = {i: numbers.count(i) for i in numbers}
    items = list(numbers_dict.items())

    n = len(items)
    for i in range(n):
        for j in range(0, n-i-1):
            if items[j][1] < items[j+1][1]:
                items[j], items[j+1] = items[j+1], items[j]

    return {i[0]: i[1] for i in items}

numbers = [int(i) for i in input("Enter list  of numbers: ").split()]
sorted_numbers = sort_by_freqency(numbers)

for number, frequency in sorted_numbers.items():
    print(f"number {number}, total: {frequency}")