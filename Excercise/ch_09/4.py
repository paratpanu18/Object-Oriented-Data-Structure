str_dict = {}
raw = input("Enter Input : ").split()

for word in raw:
    for c in word:
        if c.isalpha():
            str_dict[c] = word


def sort_dict_by_key(input_dict):
    keys = list(input_dict.keys())
    
    # BBsort
    n = len(keys)
    for i in range(n):
        for j in range(0, n-i-1):
            if keys[j] > keys[j+1]:
                keys[j], keys[j+1] = keys[j+1], keys[j]
    
    sorted_dict = {}
    for key in keys:
        sorted_dict[key] = input_dict[key]
    
    return sorted_dict

sorted_dict = sort_dict_by_key(str_dict)

for k,v in sorted_dict.items():
    print(v, end=" ")