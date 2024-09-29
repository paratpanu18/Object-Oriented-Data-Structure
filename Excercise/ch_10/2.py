number_list, keys = input("Enter Input : ").split('/')

number_list = [int(i) for i in number_list.split()]
keys = [int(i) for i in keys.split()]

number_list.sort()

def find_greater(sorted_list, key):
    for number in sorted_list:
         if number > key:
             return number
    return "No First Greater Value"

for key in keys:
    print(find_greater(number_list, key))