def binary_search(list, target, low, high):
    if low > high:
        return False
    
    mid = (low + high) // 2

    # Found target in list
    if list[mid] == target:
        return True
    
    elif target < list[mid]:
        return binary_search(list, target, low, mid - 1)
    
    elif target > list[mid]:
        return binary_search(list, target, mid + 1, high)
    
inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
print(binary_search(sorted(arr), k, 0, len(arr) - 1))