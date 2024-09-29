def print_pattern(target, current):
    if current:
        print(current)
        if current[-1] != target:
            print_pattern(target, current + chr(ord(current[-1]) + 1))
            print(current)

target = input("Enter input: ")
print_pattern(target.upper(), 'A')