def can_divide(weights, k, max_weight):
    current_sum = 0
    boxes_used = 1
    
    for weight in weights:
        if current_sum + weight > max_weight:
            boxes_used += 1
            current_sum = weight
            if boxes_used > k:
                return False
        else:
            current_sum += weight
    
    return True

def find_min_max_weight(weights, k):
    left, right = max(weights), sum(weights)
    answer = right
    
    while left <= right:
        mid = (left + right) // 2
        if can_divide(weights, k, mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return answer

input_data = input("Enter Input : ").split('/')
weights = list(map(int, input_data[0].split()))
k = int(input_data[1])

min_weight = find_min_max_weight(weights, k)

print(f"Minimum weigth for {k} box(es) = {min_weight}")
