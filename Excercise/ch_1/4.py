lst_input = [

    ["-","-","-","-","-"],

    ["-","-","-","-","-"],

    ["-","-","#","-","-"],

    ["-","-","-","-","-"],

    ["-","-","-","-","-"]

]

direction = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 0), (0, 1),
    (1, -1), (1, 0), (1, 1)
]

def num_grid(lst):

    ans = []

    for row in range(5):
        row_ans = []
        for col in range(5):
            
            '''Check if that position is a bomb'''
            if lst[row][col] == '#':
                row_ans[col] = '#'
                continue

            for row_shift, col_shift in direction:
                

                sum = 0
            
            
            ans.append(row_ans)



    return ans




# lst_input = []

# input_list = input().split(",")

# for e in input_list:
#   lst_input.append([i for i in e.split()])

print("\n",*lst_input,sep = "\n")
print("\n",*num_grid(lst_input),sep = "\n")